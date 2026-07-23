
"""
Integration test for OSPFAnalyzer.
"""

from services.analyzer.analyzers.ospf_analyzer import OSPFAnalyzer
from services.parser.parser_service import ParserService

from utils.logger import logger


def print_findings(findings):
    """
    Print analyzer findings.
    """

    print("\n" + "=" * 80)
    print("OSPF ANALYZER FINDINGS")
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
    Test OSPFAnalyzer.
    """

    logger.info("Starting OSPFAnalyzer integration test...")

    config = """
!
hostname Router1
!
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
!
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)

    analyzer = OSPFAnalyzer()

    findings = analyzer.analyze(parsed_config)

    print_findings(findings)


if __name__ == "__main__":
    main()