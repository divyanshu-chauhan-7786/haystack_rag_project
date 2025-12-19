from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack.components.converters import PyPDFToDocument

from QASystem.utils import pinecone_config


def ingestion_pipeline(document_store):
    indexing_pipeline = Pipeline()

    indexing_pipeline.add_component("converter", PyPDFToDocument())
    indexing_pipeline.add_component(
        "splitter",
        DocumentSplitter(split_by="sentence", split_length=2)
    )
    indexing_pipeline.add_component(
        "embedder",
        SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2"

        )
    )
    indexing_pipeline.add_component(
        "writer",
        DocumentWriter(document_store)
    )

    indexing_pipeline.connect("converter.documents", "splitter.documents")
    indexing_pipeline.connect("splitter.documents", "embedder.documents")
    indexing_pipeline.connect("embedder.documents", "writer.documents")

    indexing_pipeline.run({
        "converter": {
            "sources": ["./data/Transformer.pdf"]

        }
    })


if __name__ == "__main__":
    document_store = pinecone_config()
    ingestion_pipeline(document_store)
