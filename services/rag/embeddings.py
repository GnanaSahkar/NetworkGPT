"""
Embedding Service for NetworkGPT.

Generates embeddings using Google's Gemini Embedding API.
"""

from google import genai

from config.settings import settings
from utils.logger import logger


class EmbeddingService:
    """
    Handles embedding generation for documents and queries.
    """

    def __init__(self):
        logger.info("Initializing Embedding Service...")

        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

        self.model = settings.EMBEDDING_MODEL

        logger.success("Embedding Service initialized successfully.")

    def embed_query(self, query: str) -> list[float]:
        """
        Generate an embedding for a search query.
        """

        logger.info("Generating query embedding...")

        try:
            response = self.client.models.embed_content(
                model=self.model,
                contents=query,
            )

            logger.success("Query embedding generated successfully.")

            return response.embeddings[0].values

        except Exception as error:
            logger.error(f"Embedding generation failed: {error}")
            raise

    def embed_documents(
        self,
        documents,
    ):
        """
        Generate embeddings for multiple document chunks.

        Args:
            documents: List of split document chunks.

        Returns:
            List of embedding vectors.
        """

        logger.info(
            f"Generating embeddings for {len(documents)} documents..."
        )

        embeddings = []

        for document in documents:
            embedding = self.embed_query(
                document.page_content
            )

            embeddings.append(embedding)

        logger.success(
            f"Generated {len(embeddings)} document embeddings."
        )

        return embeddings