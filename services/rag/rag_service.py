
"""
RAG Service for NetworkGPT.

Coordinates retrieval and AI generation to answer
user questions using the knowledge base.
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
        Initialize the RAG Service.
        """

        logger.info("Initializing RAG Service...")

        self.retriever = Retriever()
        self.prompt_manager = PromptManager()
        self.ai_service = AIService()

        logger.success("RAG Service initialized successfully.")

    def ask(
        self,
        question: str,
    ) -> str:
        """
        Answer a question using Retrieval-Augmented Generation.

        Args:
            question: User question.

        Returns:
            AI generated answer based on retrieved context.
        """

        logger.info("Retrieving relevant context...")

        results = self.retriever.retrieve(
            query=question,
        )

        context = "\n\n".join(
            results["documents"][0]
        )

        logger.info("Creating RAG prompt...")

        prompt = self.prompt_manager.create_rag_prompt(
            context=context,
            question=question,
        )

        logger.info("Generating AI response...")

        answer = self.ai_service.ask(prompt)

        logger.success("RAG response generated successfully.")

        return answer