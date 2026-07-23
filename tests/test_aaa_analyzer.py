"""
Integration test for AAAAnalyzer.
"""

from services.parser.parser_service import ParserService
from services.analyzer.analyzers.aaa_analyzer import AAAAnalyzer

from utils.logger import logger


def print_findings(findings):
    """
    Print analyzer findings.
    """

    print("\n" + "=" * 80)
    print("AAA ANALYZER FINDINGS")
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
    Test AAAAnalyzer.
    """

    logger.info("Starting AAAAnalyzer integration test...")

    config = """
!
hostname Router1
!
aaa new-model
!
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)

    analyzer = AAAAnalyzer()

    findings = analyzer.analyze(parsed_config)

    print_findings(findings)


if __name__ == "__main__":
    main()