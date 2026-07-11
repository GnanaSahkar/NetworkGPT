
"""Text splitter module for splitting text into chunks for RAG."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import settings
from utils.logger import logger


class textsplitter:
    """Split docs into chunks for RAG."""
    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )
    def split_documents(self, loaded_documents: list[Document]) -> list[Document]:
        """
        Split loaded documents into smaller chunks.
        """

        logger.info("Splitting documents into chunks...")

        split_documents = self.splitter.split_documents(loaded_documents)

        logger.success(
            f"Created {len(split_documents)} document chunks."
        )

        return split_documents