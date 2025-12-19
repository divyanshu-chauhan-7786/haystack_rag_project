from haystack import Pipeline
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.builders import PromptBuilder
from dotenv import load_dotenv
import google.generativeai as genai
import os

from QASystem.utils import pinecone_config

load_dotenv()

# Configure Gemini directly (NO Haystack generator)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")

prompt_template = """Answer the following query using the provided context.
If the answer is not in the context, say "I don't know".

Context:
{% for doc in documents %}
{{ doc.content }}
{% endfor %}

Question: {{query}}
"""

def get_response(query):
    pipeline = Pipeline()

    pipeline.add_component(
        "text_embedder",
        SentenceTransformersTextEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    pipeline.add_component(
        "retriever",
        PineconeEmbeddingRetriever(
            document_store=pinecone_config(),
            top_k=5
        )
    )

    pipeline.add_component(
        "prompt_builder",
        PromptBuilder(
            template=prompt_template,
            required_variables=["query", "documents"]
        )
    )

    pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    pipeline.connect("retriever.documents", "prompt_builder.documents")

    result = pipeline.run({
        "text_embedder": {"text": query},
        "prompt_builder": {"query": query}
    })

    prompt = result["prompt_builder"]["prompt"]

    # 🔥 Gemini call (outside Haystack)
    response = model.generate_content(prompt)

    return response.text


if __name__ == "__main__":
    print(get_response("What is a Transformer model?"))
