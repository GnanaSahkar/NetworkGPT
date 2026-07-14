

""" AAA Parser."""

from services.parser.models import AAA
from utils.logger import logger
from services.parser.base_parser import BaseParser

class AAAParser(BaseParser):
    
    def __init__(self):
        logger.info("Initializing AAA Parser...")

        logger.success("AAA Parser initialized successfully.")
        
    def parse(
        self,
        config: str,
    ) -> AAA:
        """
        Parse AAA configuration.

        Args:
            config: AAA configuration block.

        Returns:
            AAA model.
        """

        logger.info("Parsing AAA configuration...")

        aaa = AAA()

        lines = config.splitlines()

        for index, line in enumerate(lines):

            line = line.strip()

            if not line:
                continue

            if line.startswith("aaa authentication"):
                aaa.authentication.append(
                    line.replace("aaa authentication", "", 1).strip()
                )

            elif line.startswith("aaa authorization"):
                aaa.authorization.append(
                    line.replace("aaa authorization", "", 1).strip()
                )

            elif line.startswith("aaa accounting"):
                aaa.accounting.append(
                    line.replace("aaa accounting", "", 1).strip()
                )

            elif line.startswith("radius server"):

                if index + 1 < len(lines):

                    next_line = lines[index + 1].strip()

                    if next_line.startswith("address ipv4"):

                        parts = next_line.split()

                        if len(parts) >= 3:
                            aaa.radius_servers.append(parts[2])

            elif line.startswith("tacacs server"):

                if index + 1 < len(lines):

                    next_line = lines[index + 1].strip()

                    if next_line.startswith("address ipv4"):

                        parts = next_line.split()

                        if len(parts) >= 3:
                            aaa.tacacs_servers.append(parts[2])

        logger.success("AAA configuration parsed successfully.")

        return aaa