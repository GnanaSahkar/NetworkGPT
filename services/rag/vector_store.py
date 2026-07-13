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

        self.collection = self.client.get_or_create_collection(
            name=settings.COLLECTION_NAME
        )

        logger.success("Vector Store initialized successfully.")

    def add_documents(
        self,
        documents,
        embeddings,
    ):
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
            f"Adding {len(documents)} documents to Vector Store..."
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
            f"{len(documents)} documents added successfully."
        )

    def similarity_search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ):
        """
        Perform semantic similarity search.

        Args:
            embedding: Query embedding vector.
            top_k: Number of similar chunks to retrieve.

        Returns:
            Similarity search results.
        """

        logger.info("Searching Vector Store...")

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        logger.success("Similarity search completed.")

        return results

    def count(self) -> int:
        """
        Return the number of stored document chunks.
        """

        pass

    def reset(self):
        """
        Delete all documents from the collection.
        """

        pass