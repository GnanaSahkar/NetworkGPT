
"""
BGP Parser for NetworkGPT.

Parses Cisco BGP configurations into
structured BGP models.
"""

from services.parser.base_parser import BaseParser
from services.parser.models import BGP
from utils.logger import logger


class BGPParser(BaseParser):
    """
    Parses Cisco BGP configurations.
    """

    def __init__(self):
        """
        Initialize the BGP Parser.
        """

        logger.info("Initializing BGP Parser...")
        logger.success("BGP Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> BGP:
        """
        Parse BGP configuration.

        Args:
            config: BGP configuration block.

        Returns:
            BGP model.
        """

        logger.info("Parsing BGP configuration...")

        bgp = None

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("router bgp"):

                as_number = int(line.split()[2])

                bgp = BGP(
                    as_number=as_number,
                )

            elif bgp and line.startswith("bgp router-id"):

                bgp.router_id = line.split()[2]

            elif bgp and line.startswith("neighbor"):

                parts = line.split()

                if len(parts) >= 2:
                    bgp.neighbors.append(parts[1])

            elif bgp and line.startswith("network"):

                bgp.networks.append(
                    line.replace(
                        "network",
                        "",
                        1,
                    ).strip()
                )

        logger.success("BGP configuration parsed successfully.")

        return bgp