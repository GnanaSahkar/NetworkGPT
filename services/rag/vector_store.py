"""
Vector Store for NetworkGPT.

Handles storage and retrieval of document embeddings
using ChromaDB.
"""

import chromadb

from config.settings import settings
from utils.logger import logger


class VectorStore:
    """
    Handles storage and retrieval of document embeddings.
    """

    def __init__(self):
        """
        Initialize the Vector Store with a persistent ChromaDB client.
        """

        logger.info("Initializing Vector Store...")

        self.client = chromadb.PersistentClient(
            path=str(settings.VECTOR_DB_DIR)
        )

        self.collection_name = settings.COLLECTION_NAME

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

        logger.success(
            "Vector Store initialized successfully."
        )

    def add_documents(
        self,
        documents,
        embeddings,
    ) -> None:
        """
        Store document chunks and their embeddings.

        Args:
            documents: List of split document chunks.
            embeddings: List of embedding vectors.
        """

        if len(documents) != len(embeddings):
            raise ValueError(
                "Number of documents and embeddings must be equal."
            )

        logger.info(
            f"Adding {len(documents)} document chunks..."
        )

        ids = [
            f"doc_{index}"
            for index in range(len(documents))
        ]

        texts = [
            document.page_content
            for document in documents
        ]

        metadatas = [
            document.metadata
            for document in documents
        ]

        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        logger.success(
            f"{len(documents)} document chunks added successfully."
        )

    def similarity_search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> dict:
        """
        Perform semantic similarity search.

        Args:
            embedding: Query embedding vector.
            top_k: Number of similar chunks to retrieve.

        Returns:
            Similarity search results.
        """

        logger.info(
            "Searching Vector Store..."
        )

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        logger.success(
            "Similarity search completed."
        )

        return results

    def count(self) -> int:
        """
        Return the number of document chunks stored
        in the collection.

        Returns:
            Number of indexed document chunks.
        """

        logger.info(
            "Counting indexed document chunks..."
        )

        count = self.collection.count()

        logger.success(
            f"Vector Store contains {count} document chunks."
        )

        return count

    def reset(self) -> None:
        """
        Reset the Vector Store by recreating
        the collection.
        """

        logger.info(
            f"Resetting collection '{self.collection_name}'..."
        )

        self.client.delete_collection(
            name=self.collection_name
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

        logger.success(
            f"Collection '{self.collection_name}' reset successfully."
        )