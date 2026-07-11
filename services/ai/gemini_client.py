"""
Gemini AI Client for NetworkGPT.

This module provides an implementation of the BaseAIClient
using Google's Gemini API.
"""

from google import genai

from config.settings import settings
from services.ai.base_client import BaseAIClient
from utils.logger import logger


class GeminiAIClient(BaseAIClient):
    """
    Gemini implementation of the BaseAIClient.
    """

    def __init__(self):
        """
        Initialize the Gemini AI client.
        """

        logger.info("Initializing Gemini AI Client...")

        self.api_key = settings.gemini_api_key
        self.model_name = settings.model_name

        if not self.api_key:
            logger.error("Gemini API key not found.")
            raise ValueError("Gemini API key not configured.")

        self.genai_client = genai.Client(api_key=self.api_key)

        logger.success("Gemini AI Client initialized successfully.")

    def generate_text(self, prompt: str) -> str:
        """
        Generate a text response from Gemini.

        Args:
            prompt: Input prompt.

        Returns:
            AI generated response.
        """

        logger.info("Sending prompt to Gemini...")

        try:
            response = self.genai_client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )

            logger.success("Response received from Gemini.")

            return response.text

        except Exception as error:
            logger.exception(f"Gemini request failed: {error}")
            raise

    def health_check(self) -> bool:
        """
        Verify that Gemini is reachable.

        Returns:
            True if Gemini is available, otherwise False.
        """

        try:
            response = self.genai_client.models.generate_content(
                model=self.model_name,
                contents="Reply with only OK.",
            )

            return response.text.strip().upper() == "OK"

        except Exception:
            return False