
"""
ACL Parser for NetworkGPT.
"""

from services.parser.base_parser import BaseParser
from services.parser.models import ACL
from utils.logger import logger


class ACLParser(BaseParser):

    def __init__(self):

        logger.info("Initializing ACL Parser...")
        logger.success("ACL Parser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> list[ACL]:

        logger.info("Parsing ACL configuration...")

        acls = []
        current_acl = None

        for line in config.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("ip access-list"):

                if current_acl:
                    acls.append(current_acl)

                parts = line.split()

                current_acl = ACL(
                    acl_type=parts[2],
                    name=parts[3],
                )

            elif current_acl:

                current_acl.entries.append(line)

        if current_acl:
            acls.append(current_acl)

        logger.success(
            f"{len(acls)} ACL(s) parsed successfully."
        )

        return acls