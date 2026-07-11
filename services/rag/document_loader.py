
"""Document Loader"""

#loads docs from the knowledge base

from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)

from config.settings import settings
from utils.logger import logger

class DocumentLoader:
    """
    Loads documents from the knowledge base.
    """

    def __init__(self):
        self.docs_dir = settings.DOCS_DIR

    def load_documents(self) -> list[Document]:
        """
        Load all supported documents from the knowledge base.

        Returns:
            List of Document objects.
        """

        documents = []

        logger.info("Loading knowledge base documents...")

        if not self.docs_dir.exists():
            logger.warning(f"Knowledge base directory not found: {self.docs_dir}")
            return documents

        for file_path in self.docs_dir.rglob("*"):

            if not file_path.is_file():
                continue

            suffix = file_path.suffix.lower()

            try:

                if suffix == ".pdf":
                    documents.extend(self._load_pdf(file_path))

                elif suffix in [".txt", ".md"]:
                    documents.extend(self._load_text(file_path))

            except Exception as error:
                logger.error(f"Failed to load {file_path.name}: {error}")

        logger.success(f"Loaded {len(documents)} document chunks.")

        return documents

    def _load_pdf(self, file_path: Path) -> list[Document]:
        """
        Load a PDF document.
        """

        logger.info(f"Loading PDF: {file_path.name}")

        loader = PyPDFLoader(str(file_path))

        return loader.load()

    def _load_text(self, file_path: Path) -> list[Document]:
        """
        Load a text or markdown document.
        """

        logger.info(f"Loading Text: {file_path.name}")

        loader = TextLoader(
            str(file_path),
            encoding="utf-8"
        )

        return loader.load()


