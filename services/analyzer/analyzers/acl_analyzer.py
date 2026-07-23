"""
ACL configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, ACL

from utils.logger import logger


class ACLAnalyzer(BaseAnalyzer):
    """
    Analyzer for Access Control List (ACL) configurations.
    """

    def __init__(self):
        logger.info("Initializing ACLAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze ACL configurations.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of ACL-related findings.
        """

        logger.info("Analyzing ACL configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_empty_acls(parsed_config.acls)
        )

        findings.extend(
            self._check_permit_any_any(parsed_config.acls)
        )

        logger.success(
            f"ACL analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_empty_acls(
        self,
        acls: list[ACL],
    ) -> list[Finding]:
        """
        Check for ACLs without any entries.
        """

        findings: list[Finding] = []

        for acl in acls:

            entries = [
                entry.strip()
                for entry in acl.entries
                if entry.strip()
            ]

            if not entries:

                findings.append(
                    self._create_finding(
                        category="ACL",
                        severity="Medium",
                        title="Empty Access Control List",
                        description=(
                            f"ACL '{acl.name}' contains no access control entries."
                        ),
                        recommendation=(
                            "Add the required ACL entries or remove the unused ACL."
                        ),
                    )
                )

        return findings

    def _check_permit_any_any(
        self,
        acls: list[ACL],
    ) -> list[Finding]:
        """
        Check for overly permissive ACL entries.
        """

        findings: list[Finding] = []

        for acl in acls:

            entries = [
                entry.strip().lower()
                for entry in acl.entries
                if entry.strip()
            ]

            for entry in entries:

                if (
                    "permit ip any any" in entry
                    or "permit any any" in entry
                ):

                    findings.append(
                        self._create_finding(
                            category="ACL",
                            severity="High",
                            title="Overly Permissive ACL Rule",
                            description=(
                                f"ACL '{acl.name}' contains the rule '{entry}', "
                                "which permits unrestricted traffic."
                            ),
                            recommendation=(
                                "Replace the rule with more restrictive access control entries "
                                "that follow the principle of least privilege."
                            ),
                        )
                    )

        return findings

    @staticmethod
    def _create_finding(
        category: str,
        severity: str,
        title: str,
        description: str,
        recommendation: str,
    ) -> Finding:
        """
        Create a Finding object.
        """

        return Finding(
            category=category,
            severity=severity,
            title=title,
            description=description,
            recommendation=recommendation,
        )