"""
Interface Parser for NetworkGPT.

Parses Cisco interface configurations into
structured Interface models.
"""

from services.parser.models import Interface
from utils.logger import logger


class InterfaceParser:
    """
    Parses Cisco interface configurations.
    """

    def __init__(self):

        logger.info("Initializing Interface Parser...")

        logger.success("Interface Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> Interface:
        """
        Parse a single interface configuration.

        Args:
            config: Interface configuration block.

        Returns:
            Interface model.
        """

        logger.info("Parsing interface configuration...")

        interface = Interface(name="")

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("interface"):
                interface.name = line.split(maxsplit=1)[1]

            elif line.startswith("description"):
                interface.description = line.replace(
                    "description",
                    "",
                    1,
                ).strip()

            elif line.startswith("ip address"):

                parts = line.split()

                if len(parts) >= 4:
                    interface.ip_address = parts[2]
                    interface.subnet_mask = parts[3]

            elif line.startswith("shutdown"):
                interface.shutdown = True

            elif line.startswith("no shutdown"):
                interface.shutdown = False

            elif line.startswith("speed"):
                interface.speed = line.split(maxsplit=1)[1]

            elif line.startswith("duplex"):
                interface.duplex = line.split(maxsplit=1)[1]

            elif line.startswith("switchport access vlan"):

                interface.vlan = line.split()[-1]

        logger.success(
            f"Interface '{interface.name}' parsed successfully."
        )

        return interface