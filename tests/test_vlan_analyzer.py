
"""
Integration test for VLANAnalyzer.
"""

from services.parser.parser_service import ParserService
from services.analyzer.analyzers.vlan_analyzer import VLANAnalyzer

from utils.logger import logger


def print_findings(findings):
    """
    Print analyzer findings.
    """

    print("\n" + "=" * 80)
    print("VLAN ANALYZER FINDINGS")
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
    print(f"Total Findings: {len(findings)}")
    print("=" * 80)


def main():
    """
    Test VLANAnalyzer.
    """

    logger.info("Starting VLANAnalyzer integration test...")

    config = """
!
hostname Router1
!
vlan 10
!
vlan 20
 name USERS
!
vlan 30
 name SERVERS
!
interface GigabitEthernet0/1
 switchport access vlan 20
!
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)

    analyzer = VLANAnalyzer()

    findings = analyzer.analyze(parsed_config)

    print_findings(findings)


if __name__ == "__main__":
    main()