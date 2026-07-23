
from abc import ABC, abstractmethod

from services.parser.models import ParsedConfig
from services.analyzer.models import Finding


class BaseAnalyzer(ABC):
    """
    Abstract base class for all analyzers.
    """

    @abstractmethod
    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze the parsed configuration and return findings.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            list[Finding]: List of analysis findings.
        """
        pass