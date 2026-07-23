"""
Integration test for AnalyzerService.
"""

from services.analyzer.analyzer_service import AnalyzerService
from services.parser.parser_service import ParserService

from utils.logger import logger


def print_findings(findings):
    """
    Print analyzer findings.
    """

    print("\n" + "=" * 80)
    print("NETWORK ANALYSIS REPORT")
    print("=" * 80)

    if not findings:
        print("No findings.")
        return

    for index, finding in enumerate(findings, start=1):

        print(f"\nFinding #{index}")
        print("-" * 80)
        print(f"Category       : {finding.category}")
        print(f"Severity       : {finding.severity}")
        print(f"Title          : {finding.title}")
        print(f"Description    : {finding.description}")
        print(f"Recommendation : {finding.recommendation}")

    print("\n" + "=" * 80)
    print(f"Total Findings : {len(findings)}")
    print("=" * 80)


def main():
    """
    Test AnalyzerService.
    """

    logger.info("Starting AnalyzerService integration test...")

    config = """
!
hostname Router1
!
aaa new-model
!
vlan 10
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
!
interface GigabitEthernet0/1
 description LAN Interface
 shutdown
!
ip access-list extended INTERNET
 permit ip any any
!
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
!
router bgp 65001
!
ip route 10.0.0.0 255.255.255.0 192.168.1.1
ip route 10.0.0.0 255.255.255.0 192.168.1.1
!
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)

    analyzer_service = AnalyzerService()

    analysis_report = analyzer_service.analyze(parsed_config)

    print_findings(
        analysis_report.findings
    )


if __name__ == "__main__":
    main()