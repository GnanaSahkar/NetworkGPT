"""
Test the complete RAG ingestion pipeline.
"""

from services.rag.document_loader import DocumentLoader
from services.rag.text_splitter import textsplitter as TextSplitter
from services.rag.embeddings import EmbeddingService
from services.rag.vector_store import VectorStore
from utils.logger import logger


def main():
    """
    Execute the complete RAG ingestion pipeline.
    """

    loader = DocumentLoader()
    splitter = TextSplitter()
    embedder = EmbeddingService()
    vector_store = VectorStore()

    # Reset existing collection
    vector_store.reset()

    # Load documents
    documents = loader.load_documents()
    logger.info(f"Loaded Documents : {len(documents)}")

    # Split documents
    chunks = splitter.split_documents(documents)
    logger.info(f"Split Documents : {len(chunks)}")

    # Generate embeddings
    embeddings = embedder.embed_documents(chunks)
    logger.info(
        f"Generated Embeddings : {len(embeddings)}"
    )

    # Store embeddings
    vector_store.add_documents(
        documents=chunks,
        embeddings=embeddings,
    )

    logger.success(
        "Knowledge Base indexed successfully."
    )

    logger.info(
        f"Indexed Chunks : {vector_store.count()}"
    )


if __name__ == "__main__":
    main()