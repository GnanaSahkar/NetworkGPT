
"""
VLAN Parser for NetworkGPT.

Parses Cisco VLAN configurations into
structured VLAN models.
"""

from services.parser.base_parser import BaseParser
from services.parser.models import VLAN
from utils.logger import logger


class VLANParser(BaseParser):
    """
    Parses Cisco VLAN configurations.
    """

    def __init__(self):
        logger.info("Initializing VLAN Parser...")
        logger.success("VLAN Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> list[VLAN]:
        """
        Parse VLAN configuration.

        Args:
            config: VLAN configuration block.

        Returns:
            List of VLAN models.
        """

        logger.info("Parsing VLAN configuration...")

        vlans = []
        current_vlan = None

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("vlan "):

                if current_vlan:
                    vlans.append(current_vlan)

                vlan_id = int(line.split()[1])

                current_vlan = VLAN(
                    vlan_id=vlan_id,
                )

            elif line.startswith("name") and current_vlan:

                current_vlan.name = line.replace(
                    "name",
                    "",
                    1,
                ).strip()

        if current_vlan:
            vlans.append(current_vlan)

        logger.success(
            f"{len(vlans)} VLAN(s) parsed successfully."
        )

        return vlans