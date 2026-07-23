"""
BGP configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, BGP

from utils.logger import logger


class BGPAnalyzer(BaseAnalyzer):
    """
    Analyzer for BGP configurations.
    """

    def __init__(self):
        logger.info("Initializing BGPAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze BGP configuration.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of BGP-related findings.
        """

        logger.info("Analyzing BGP configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_router_id(parsed_config.bgp)
        )

        findings.extend(
            self._check_neighbors(parsed_config.bgp)
        )

        findings.extend(
            self._check_networks(parsed_config.bgp)
        )

        logger.success(
            f"BGP analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_router_id(
        self,
        bgp: BGP | None,
    ) -> list[Finding]:
        """
        Check whether a BGP router ID is configured.
        """

        findings: list[Finding] = []

        if bgp is None:
            return findings

        if not bgp.router_id.strip():

            findings.append(
                self._create_finding(
                    category="BGP",
                    severity="Medium",
                    title="Missing BGP Router ID",
                    description=(
                        "BGP is configured without an explicit router ID."
                    ),
                    recommendation=(
                        "Configure a unique BGP router ID."
                    ),
                )
            )

        return findings

    def _check_neighbors(
        self,
        bgp: BGP | None,
    ) -> list[Finding]:
        """
        Check whether BGP neighbors are configured.
        """

        findings: list[Finding] = []

        if bgp is None:
            return findings

        neighbors = [
            neighbor.strip()
            for neighbor in bgp.neighbors
            if neighbor.strip()
        ]

        if not neighbors:

            findings.append(
                self._create_finding(
                    category="BGP",
                    severity="High",
                    title="No BGP Neighbors Configured",
                    description=(
                        "No BGP neighbors are configured."
                    ),
                    recommendation=(
                        "Configure at least one BGP neighbor to establish BGP peering."
                    ),
                )
            )

        return findings

    def _check_networks(
        self,
        bgp: BGP | None,
    ) -> list[Finding]:
        """
        Check whether BGP network statements are configured.
        """

        findings: list[Finding] = []

        if bgp is None:
            return findings

        networks = [
            network.strip()
            for network in bgp.networks
            if network.strip()
        ]

        if not networks:

            findings.append(
                self._create_finding(
                    category="BGP",
                    severity="Medium",
                    title="No Advertised BGP Networks",
                    description=(
                        "No network statements are configured for BGP."
                    ),
                    recommendation=(
                        "Configure BGP network statements to advertise the required prefixes."
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