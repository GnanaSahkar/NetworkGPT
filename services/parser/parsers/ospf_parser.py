

"""
OSPF Parser for NetworkGPT.
"""

from services.parser.base_parser import BaseParser
from services.parser.models import OSPF
from utils.logger import logger


class OSPFParser(BaseParser):

    def __init__(self):

        logger.info("Initializing OSPF Parser...")
        logger.success("OSPF Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> OSPF:

        logger.info("Parsing OSPF configuration...")

        ospf = None

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("router ospf"):

                process_id = int(line.split()[2])

                ospf = OSPF(
                    process_id=process_id,
                )

            elif ospf and line.startswith("router-id"):

                ospf.router_id = line.split()[1]

            elif ospf and line.startswith("network"):

                ospf.networks.append(
                    line.replace(
                        "network",
                        "",
                        1,
                    ).strip()
                )

            elif ospf and line.startswith("passive-interface"):

                ospf.passive_interfaces.append(
                    line.split()[1]
                )

        logger.success("OSPF parsed successfully.")

        return ospf