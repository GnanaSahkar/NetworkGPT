
from services.parser.config_parser import ConfigParser

from services.parser.models import ParsedConfig

from utils.logger import logger


class ParserService:
    """
    Public entry point for the parser framework.
    """

    def __init__(self):
        logger.info("Initializing ParserService...")

        self.config_parser = ConfigParser()

        logger.success("ParserService initialized successfully.")

    def parse_config(
        self,
        config: str,
    ) -> ParsedConfig:
        """
        Parse an entire Cisco configuration.

        Args:
            config: Raw Cisco configuration.

        Returns:
            ParsedConfig
        """

        logger.info("Starting configuration parsing...")

        parsed_config = self.config_parser.parse(config)

        logger.success("Configuration parsing completed.")

        return parsed_config