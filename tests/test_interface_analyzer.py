

from services.parser.parser_service import ParserService
from services.analyzer.analyzers.interface_analyzer import InterfaceAnalyzer

from utils.logger import logger


def main():

    logger.info("Starting InterfaceAnalyzer test...")

    config = """
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown

interface GigabitEthernet0/1
 description LAN Interface
 shutdown

interface GigabitEthernet0/2
 description WAN Interface
 ip address 10.0.0.1 255.255.255.0
 no shutdown
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)
    
    """print(type(parsed_config.interfaces))
    print(parsed_config.interfaces)"""

    analyzer = InterfaceAnalyzer()

    findings = analyzer.analyze(parsed_config)

    print()
    print("=" * 80)
    print("INTERFACE ANALYZER")
    print("=" * 80)

    for finding in findings:
        print("-" * 80)
        print(f"Category       : {finding.category}")
        print(f"Severity       : {finding.severity}")
        print(f"Title          : {finding.title}")
        print(f"Description    : {finding.description}")
        print(f"Recommendation : {finding.recommendation}")


if __name__ == "__main__":
    main()