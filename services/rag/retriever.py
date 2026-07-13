"""
Retriever for NetworkGPT.

Retrieves the most relevant document chunks
from the vector database.
"""

from services.rag.embeddings import EmbeddingService
from services.rag.vector_store import VectorStore
from utils.logger import logger


class Retriever:
    """
    Handles semantic retrieval from ChromaDB.
    """

    def __init__(self):
        logger.info("Initializing Retriever...")

        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

        logger.success("Retriever initialized successfully.")

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):
        """
        Retrieve the most relevant document chunks.

        Args:
            query: User question.
            top_k: Number of chunks to retrieve.

        Returns:
            ChromaDB search results.
        """

        

        query_embedding = self.embedding_service.embed_query(
            query
        )

        

        results = self.vector_store.similarity_search(
            embedding=query_embedding,
            top_k=top_k,
        )

        logger.success("Relevant documents retrieved.")

        return results