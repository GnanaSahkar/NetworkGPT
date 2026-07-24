"""
RAG Service for NetworkGPT.

Provides Retrieval-Augmented Generation (RAG) functionality by
retrieving relevant documentation from the knowledge base and,
optionally, generating AI responses.
"""

from services.ai.ai_service import AIService
from services.ai.prompt_manager import PromptManager
from services.rag.retriever import Retriever
from utils.logger import logger


class RAGService:
    """
    Coordinates Retrieval-Augmented Generation (RAG).
    """

    def __init__(self):
        """
        Initialize the RAG service.
        """

        logger.info("Initializing RAG Service...")

        self.retriever = Retriever()
        self.prompt_manager = PromptManager()
        self.ai_service = AIService()

        logger.success("RAG Service initialized successfully.")

    def retrieve_context(
        self,
        query: str,
    ) -> str:
        """
        Retrieve relevant documentation from the knowledge base.

        Args:
            query: Search query.

        Returns:
            Retrieved context as a single string.
        """

        logger.info(
            f"Retrieving context for query: {query}"
        )

        results = self.retriever.retrieve(
            query=query,
        )

        documents = results.get(
            "documents",
            [],
        )

        if not documents or not documents[0]:
            logger.warning(
                "No relevant documents found."
            )
            return ""

        context = "\n\n".join(
            documents[0]
        )

        logger.success(
            "Context retrieved successfully."
        )

        return context

    def ask(
        self,
        question: str,
    ) -> str:
        """
        Answer a question using Retrieval-Augmented Generation.

        Args:
            question: User question.

        Returns:
            AI-generated answer.
        """

        logger.info(
            "Generating RAG response..."
        )

        context = self.retrieve_context(
            query=question,
        )

        prompt = self.prompt_manager.create_rag_prompt(
            context=context,
            question=question,
        )

        answer = self.ai_service.ask(
            prompt
        )

        logger.success(
            "RAG response generated successfully."
        )

        return answer