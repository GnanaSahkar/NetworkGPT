from services.parser.base_parser import BaseParser
from services.parser.models import Interface

from utils.logger import logger


class InterfaceParser(BaseParser):
    """
    Parser for Cisco interface configurations.
    """

    def __init__(self):
        logger.info("Initializing InterfaceParser...")

    def parse(
        self,
        config: str,
    ) -> list[Interface]:
        """
        Parse interface configurations.

        Args:
            config: Complete device configuration.

        Returns:
            List of parsed Interface objects.
        """

        logger.info("Parsing interface configurations...")

        interfaces: list[Interface] = []
        current_interface: Interface | None = None

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            # -------------------------------------------------
            # Start of a new interface block
            # -------------------------------------------------
            if line.startswith("interface"):

                # Save the previous interface before starting a new one
                if current_interface is not None:
                    interfaces.append(current_interface)

                interface_name = line.split(maxsplit=1)[1]

                current_interface = Interface(
                    name=interface_name
                )

                continue

            # Ignore lines until an interface block starts
            if current_interface is None:
                continue

            # -------------------------------------------------
            # Description
            # -------------------------------------------------
            if line.startswith("description"):

                current_interface.description = (
                    line.replace(
                        "description",
                        "",
                        1,
                    ).strip()
                )

            # -------------------------------------------------
            # IP Address
            # -------------------------------------------------
            elif line.startswith("ip address"):

                parts = line.split()

                if len(parts) >= 4:
                    current_interface.ip_address = parts[2]
                    current_interface.subnet_mask = parts[3]

            # -------------------------------------------------
            # Shutdown
            # -------------------------------------------------
            elif line == "shutdown":
                current_interface.shutdown = True

            elif line == "no shutdown":
                current_interface.shutdown = False

            # -------------------------------------------------
            # Speed
            # -------------------------------------------------
            elif line.startswith("speed"):

                current_interface.speed = (
                    line.split(maxsplit=1)[1]
                )

            # -------------------------------------------------
            # Duplex
            # -------------------------------------------------
            elif line.startswith("duplex"):

                current_interface.duplex = (
                    line.split(maxsplit=1)[1]
                )

            # -------------------------------------------------
            # Access VLAN
            # -------------------------------------------------
            elif line.startswith("switchport access vlan"):

                current_interface.vlan = line.split()[-1]

        # Save the last interface
        if current_interface is not None:
            interfaces.append(current_interface)

        logger.success(
            f"Successfully parsed {len(interfaces)} interface(s)."
        )

        return interfaces