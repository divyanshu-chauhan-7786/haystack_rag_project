from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def pinecone_config():
    """
    Returns a configured PineconeDocumentStore.
    Assumes PINECONE_API_KEY is already available in environment.
    """
    return PineconeDocumentStore(
        index="rag-minilm-384",
        namespace="default",
        dimension=384
    )
