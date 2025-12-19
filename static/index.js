async function askQuestion() {
    const questionInput = document.getElementById("question");
    const answerBox = document.getElementById("answerBox");
    const answerText = document.getElementById("answerText");
    const errorBox = document.getElementById("errorBox");
    const loading = document.getElementById("loading");
    const button = document.getElementById("askBtn");

    const question = questionInput.value.trim();

    if (!question) {
        errorBox.style.display = "block";
        errorBox.innerText = "Please enter a question.";
        return;
    }

    // Reset UI
    errorBox.style.display = "none";
    answerBox.style.display = "none";
    loading.style.display = "block";
    button.disabled = true;

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        loading.style.display = "none";
        button.disabled = false;

        if (response.ok) {
            answerBox.style.display = "block";
            answerText.innerText = data.answer;
        } else {
            errorBox.style.display = "block";
            errorBox.innerText = data.error || "Something went wrong.";
        }
    } catch (err) {
        loading.style.display = "none";
        button.disabled = false;
        errorBox.style.display = "block";
        errorBox.innerText = "Failed to connect to server.";
    }
}

// Submit on Enter (without new line)
function handleEnter(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        askQuestion();
    }
}
