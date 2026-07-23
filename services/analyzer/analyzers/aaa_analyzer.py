"""
AAA configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, AAA

from utils.logger import logger


class AAAAnalyzer(BaseAnalyzer):
    """
    Analyzer for AAA configurations.
    """

    def __init__(self):
        logger.info("Initializing AAAAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze AAA configuration.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of AAA-related findings.
        """

        logger.info("Analyzing AAA configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_aaa_configured(parsed_config.aaa)
        )

        if parsed_config.aaa is not None:

            findings.extend(
                self._check_authentication(parsed_config.aaa)
            )

            findings.extend(
                self._check_authorization(parsed_config.aaa)
            )

            findings.extend(
                self._check_accounting(parsed_config.aaa)
            )

            findings.extend(
                self._check_server_configuration(parsed_config.aaa)
            )

        logger.success(
            f"AAA analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_aaa_configured(
        self,
        aaa: AAA | None,
    ) -> list[Finding]:
        """
        Check whether AAA is configured.
        """

        findings: list[Finding] = []

        if aaa is None:

            findings.append(
                self._create_finding(
                    category="AAA",
                    severity="High",
                    title="AAA Not Configured",
                    description=(
                        "Authentication, Authorization, and Accounting (AAA) "
                        "is not configured on the device."
                    ),
                    recommendation=(
                        "Configure AAA to improve authentication, authorization, "
                        "and accounting for administrative access."
                    ),
                )
            )

        return findings

    def _check_authentication(
        self,
        aaa: AAA,
    ) -> list[Finding]:
        """
        Check AAA authentication configuration.
        """

        findings: list[Finding] = []

        authentication = [
            auth.strip()
            for auth in aaa.authentication
            if auth.strip()
        ]

        if not authentication:

            findings.append(
                self._create_finding(
                    category="AAA",
                    severity="Medium",
                    title="Missing AAA Authentication",
                    description=(
                        "No AAA authentication methods are configured."
                    ),
                    recommendation=(
                        "Configure AAA authentication to control user login."
                    ),
                )
            )

        return findings

    def _check_authorization(
        self,
        aaa: AAA,
    ) -> list[Finding]:
        """
        Check AAA authorization configuration.
        """

        findings: list[Finding] = []

        authorization = [
            auth.strip()
            for auth in aaa.authorization
            if auth.strip()
        ]

        if not authorization:

            findings.append(
                self._create_finding(
                    category="AAA",
                    severity="Medium",
                    title="Missing AAA Authorization",
                    description=(
                        "No AAA authorization methods are configured."
                    ),
                    recommendation=(
                        "Configure AAA authorization to control user privileges."
                    ),
                )
            )

        return findings

    def _check_accounting(
        self,
        aaa: AAA,
    ) -> list[Finding]:
        """
        Check AAA accounting configuration.
        """

        findings: list[Finding] = []

        accounting = [
            account.strip()
            for account in aaa.accounting
            if account.strip()
        ]

        if not accounting:

            findings.append(
                self._create_finding(
                    category="AAA",
                    severity="Medium",
                    title="Missing AAA Accounting",
                    description=(
                        "No AAA accounting methods are configured."
                    ),
                    recommendation=(
                        "Configure AAA accounting to record administrative activities."
                    ),
                )
            )

        return findings

    def _check_server_configuration(
        self,
        aaa: AAA,
    ) -> list[Finding]:
        """
        Check whether RADIUS or TACACS+ servers are configured.
        """

        findings: list[Finding] = []

        radius_servers = [
            server.strip()
            for server in aaa.radius_servers
            if server.strip()
        ]

        tacacs_servers = [
            server.strip()
            for server in aaa.tacacs_servers
            if server.strip()
        ]

        if not radius_servers and not tacacs_servers:

            findings.append(
                self._create_finding(
                    category="AAA",
                    severity="Low",
                    title="No AAA Server Configured",
                    description=(
                        "Neither RADIUS nor TACACS+ servers are configured."
                    ),
                    recommendation=(
                        "Configure a RADIUS or TACACS+ server for centralized "
                        "authentication and authorization."
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