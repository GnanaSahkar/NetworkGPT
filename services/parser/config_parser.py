from services.parser.base_parser import BaseParser
from services.parser.models import ParsedConfig

from services.parser.parsers.interface_parser import InterfaceParser
from services.parser.parsers.aaa_parser import AAAParser
from services.parser.parsers.vlan_parser import VLANParser
from services.parser.parsers.ospf_parser import OSPFParser
from services.parser.parsers.acl_parser import ACLParser
from services.parser.parsers.route_parser import RoutingParser
from services.parser.parsers.bgp_parser import BGPParser

from utils.logger import logger


class ConfigParser(BaseParser):
    """
    Coordinates all protocol-specific parsers and returns
    a structured ParsedConfig object.
    """

    def __init__(self):
        logger.info("Initializing ConfigParser...")

        self.interface_parser = InterfaceParser()
        self.aaa_parser = AAAParser()
        self.vlan_parser = VLANParser()
        self.ospf_parser = OSPFParser()
        self.acl_parser = ACLParser()
        self.routing_parser = RoutingParser()
        self.bgp_parser = BGPParser()

        logger.success("ConfigParser initialized successfully.")

    def parse(
        self,
        config: str,
    ) -> ParsedConfig:
        """
        Parse the complete Cisco configuration.

        Args:
            config: Raw Cisco configuration.

        Returns:
            ParsedConfig: Structured configuration object.
        """

        logger.info("Parsing complete configuration...")

        parsed_config = ParsedConfig()

        parsed_config.interfaces = self.interface_parser.parse(config)
        parsed_config.vlans = self.vlan_parser.parse(config)
        parsed_config.acls = self.acl_parser.parse(config)
        parsed_config.routes = self.routing_parser.parse(config)

        parsed_config.aaa = self.aaa_parser.parse(config)
        parsed_config.ospf = self.ospf_parser.parse(config)
        parsed_config.bgp = self.bgp_parser.parse(config)

        logger.success("Configuration parsed successfully.")

        return parsed_config