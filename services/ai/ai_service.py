

"""AI service module for NetworkGPT.
This is the main entry point for all the AI capabilities."""

from services.ai.gemini_client import GeminiAIClient
from services.ai.prompt_manager import PromptManager
from utils.logger import logger

class AIService:
    """AI service for NetworkGPT."""
    
    def __init__(self):
        logger.info("Initializing AI Service...")
        self.client = GeminiAIClient()
        self.prompt_manager = PromptManager()
        logger.success("AI Service initialized successfully.")
        
    def ask(self, question: str) -> str:
        prompt = self.prompt_manager.create_prompt(question)
        return self.client.generate_text(prompt)
    
    def summarize_configureation(self, configuration: str) -> str:
        prompt = self.prompt_manager.create_summary_prompt(configuration)
        return self.client.generate_text(prompt)
    
    def explain_command(self, command: str) -> str:
        prompt = self.prompt_manager.create_command_explanation_prompt(command)
        return self.client.generate_text(prompt)