from services.ai import prompt


class PromptManager:
    """
    Manages all prompt templates used by NetworkGPT.
    """

    def general_prompt(self, question: str) -> str:
        return prompt.general_prompt(question)

    def summary_prompt(self, config: str) -> str:
        return prompt.summary_prompt(config)

    def command_prompt(self, command: str) -> str:
        return prompt.command_prompt(command)

    def create_rag_prompt(
        self,
        context: str,
        question: str,
    ) -> str:
        """
        Create a Retrieval-Augmented Generation (RAG) prompt.

        Args:
            context: Retrieved document context.
            question: User question.

        Returns:
            Formatted RAG prompt.
        """

        return prompt.RAG_PROMPT.format(
            context=context,
            question=question,
        )