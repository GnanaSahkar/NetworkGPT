
"""Abstract base class for all the AI Model clients used in the system."""

from abc import ABC, abstractmethod

class BaseAIClient(ABC):
    """Abstract base class for all the AI Model clients used in the system."""

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """Generate text responce from the AI model

        Args:
            prompt (str): The input prompt to generate a response for.

        Returns:
            str: The generated response.
        """
        pass
    def embed_text(self, text: str) -> list[float]:
      """Generate embeddings for text."""
    pass
    
    def generate_text(self, prompt: str) -> str:
     pass


    def health_check(self) -> bool:
        pass