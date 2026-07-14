
"""
Base Parser for NetworkGPT.

Defines the interface for all configuration parsers.
"""

from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Abstract base class for all configuration parsers.
    """

    @abstractmethod
    def parse(
        self,
        config: str,
    ):
        """
        Parse configuration into a structured model.
        """
        pass