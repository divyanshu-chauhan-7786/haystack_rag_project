#  End-to-End RAG Application  
### FastAPI · Haystack · Pinecone · Gemini

An **end-to-end Retrieval Augmented Generation (RAG) system** that enables users to ask questions from their own documents using modern AI techniques.

This project demonstrates a **production-ready RAG pipeline** with a clean frontend, scalable backend, and secure handling of API keys.

---

##  Features

-  Document-based Question Answering  
-  Semantic Search using embeddings  
-  Context-aware responses (RAG)  
-  FastAPI backend  
-  Clean HTML/CSS/JS frontend  
-  Secure API key management using `.env`  

---

##  Project Structure

```text
End_to_end_rag/
│
├── app.py                  
├── README.md               
├── requirements.txt        
├── .gitignore              
│
├── QASystem/
│   ├── __init__.py
│   └── retrievalgeneration.py   
│
├── templates/
│   └── index.html         
│
├── static/
│   ├── index.css           
│   └── index.js          
│
└── data/                  
```
---

##  **Project Overview — End-to-End RAG Application**

**Architecture Overview:**  
This project implements a complete **Retrieval Augmented Generation (RAG)** pipeline where user queries are answered using **context retrieved from custom documents**.

**Flow:**  
**User (Browser)**  
↓  
**Frontend (HTML, CSS, JavaScript)**  
↓  
**FastAPI Backend (`/ask` endpoint)**  
↓  
**Haystack Retriever**  
↓  
**Pinecone Vector Database**  
↓  
**Relevant Context Chunks**  
↓  
**Gemini Large Language Model**  
↓  
**Final Answer to User**

---

**Tech Stack:**  
- **Backend:** FastAPI  
- **Frontend:** HTML, CSS, JavaScript  
- **Retrieval Framework:** Haystack  
- **Vector Database:** Pinecone  
- **Large Language Model:** Gemini (Google Generative AI)  
- **Embedding Model:** Sentence Transformers  

---

**Installation & Setup:**  

1. **Clone the repository**  
`git clone https://github.com/divyanshu-chauhan-7786/haystack_rag_project`  
`cd End_to_end_rag`

2. **Create a virtual environment**  
`python -m venv venv`

**Activate the environment:**  
- **Windows:** `venv\Scripts\activate`  
- **Linux / macOS:** `source venv/bin/activate`

3. **Install required dependencies**  
`pip install -r requirements.txt`

4. **Environment configuration**  
Create a **`.env` file** (**do not commit this file**) and add:  
`PINECONE_API_KEY=your_pinecone_api_key`  
`GEMINI_API_KEY=your_gemini_api_key`

---

**Running the Application:**  
Start the FastAPI development server using:  
`uvicorn app:app --reload`

Access the application in your browser:  
`http://127.0.0.1:8000`

---

**Working Principle:**  
- Documents are converted into **vector embeddings** using **Sentence Transformers**.  
- These embeddings are stored in **Pinecone** for efficient **semantic search**.  
- When a user submits a query, **relevant document chunks** are retrieved.  
- The retrieved context is passed to the **Gemini LLM**.  
- Gemini generates a **context-aware and accurate response**.

---

**Security Considerations:**  
- The **`.env` file** is excluded using **`.gitignore`**.  
- **API keys are never committed** to version control.  
- **GitHub Push Protection** is enabled to prevent secret leakage.

---

**Limitations:**  
- Best suited for **clean, text-based documents**.  
- Depends on external services like **Pinecone** and **Gemini**.  
- **Authentication and access control** are not implemented in the current version.

---

**Future Enhancements:**  
- **Conversational memory** for multi-turn interactions.  
- **Multiple document collections** support.  
- **Dark mode** user interface.  
- **Streaming LLM responses**.  
- **Cloud deployment** on Render, Railway, or AWS.

---
<img width="923" height="487" alt="image" src="https://github.com/user-attachments/assets/ad82ad0c-7272-404e-aa16-bd3867e3b84a" />

---
**Developer**  
**Divyanshu Chauhan**  
**AI / ML Engineer**  
Passionate about **Natural Language Processing**, **RAG systems**, and **real-world AI solutions**.

---

**Support & Contribution:**  
If you find this project useful, please **star the repository**, **fork it for experimentation**, or **open issues** for suggestions and improvements.


