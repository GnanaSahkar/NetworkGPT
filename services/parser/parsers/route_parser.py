
"""
Routing Parser for NetworkGPT.

Parses Cisco static route configurations into
structured Route models.
"""

from services.parser.base_parser import BaseParser
from services.parser.models import Route
from utils.logger import logger


class RoutingParser(BaseParser):
    """
    Parses Cisco static route configurations.
    """

    def __init__(self):
        """
        Initialize the Routing Parser.
        """

        logger.info("Initializing Routing Parser...")
        logger.success("Routing Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> list[Route]:
        """
        Parse static route configuration.

        Args:
            config: Routing configuration block.

        Returns:
            List of Route models.
        """

        logger.info("Parsing routing configuration...")

        routes = []

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("ip route"):

                parts = line.split()

                if len(parts) >= 5:

                    route = Route(
                        destination=parts[2],
                        subnet_mask=parts[3],
                        next_hop=parts[4],
                    )

                    routes.append(route)

        logger.success(
            f"{len(routes)} route(s) parsed successfully."
        )

        return routes