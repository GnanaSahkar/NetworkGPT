
from services.ai import prompt

class PromptManager:
    def general_prompt(self, question: str) -> str:
        return prompt.general_prompt(question)
    
    def summary_prompt(self, config: str) -> str:
        return prompt.summary_prompt(config)
    
    def command_prompt(self, command: str) -> str:
        return prompt.command_prompt(command)
    