"""
OSPF configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, OSPF

from utils.logger import logger


class OSPFAnalyzer(BaseAnalyzer):
    """
    Analyzer for OSPF configurations.
    """

    def __init__(self):
        logger.info("Initializing OSPFAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze OSPF configuration.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of OSPF-related findings.
        """

        logger.info("Analyzing OSPF configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_router_id(parsed_config.ospf)
        )

        findings.extend(
            self._check_networks(parsed_config.ospf)
        )

        findings.extend(
            self._check_passive_interfaces(parsed_config.ospf)
        )

        logger.success(
            f"OSPF analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_router_id(
        self,
        ospf: OSPF | None,
    ) -> list[Finding]:
        """
        Check whether an OSPF router ID is configured.
        """

        findings: list[Finding] = []

        if ospf is None:
            return findings

        if not ospf.router_id.strip():

            findings.append(
                self._create_finding(
                    category="OSPF",
                    severity="Medium",
                    title="Missing OSPF Router ID",
                    description=(
                        "OSPF is configured without an explicit router ID."
                    ),
                    recommendation=(
                        "Configure a unique OSPF router ID."
                    ),
                )
            )

        return findings

    def _check_networks(
        self,
        ospf: OSPF | None,
    ) -> list[Finding]:
        """
        Check whether OSPF network statements are configured.
        """

        findings: list[Finding] = []

        if ospf is None:
            return findings

        networks = [
            network.strip()
            for network in ospf.networks
            if network.strip()
        ]

        if not networks:

            findings.append(
                self._create_finding(
                    category="OSPF",
                    severity="Medium",
                    title="No OSPF Network Statements",
                    description=(
                        "No network statements are configured for the OSPF process."
                    ),
                    recommendation=(
                        "Configure OSPF network statements to advertise connected networks."
                    ),
                )
            )

        return findings

    def _check_passive_interfaces(
        self,
        ospf: OSPF | None,
    ) -> list[Finding]:
        """
        Check whether passive interfaces are configured.
        """

        findings: list[Finding] = []

        if ospf is None:
            return findings

        passive_interfaces = [
            interface.strip()
            for interface in ospf.passive_interfaces
            if interface.strip()
        ]

        if not passive_interfaces:

            findings.append(
                self._create_finding(
                    category="OSPF",
                    severity="Low",
                    title="No Passive Interfaces Configured",
                    description=(
                        "No passive interfaces are configured for the OSPF process."
                    ),
                    recommendation=(
                        "Configure passive interfaces where OSPF neighbors are not required."
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