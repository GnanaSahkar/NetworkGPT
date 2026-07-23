"""
VLAN configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, VLAN

from utils.logger import logger


class VLANAnalyzer(BaseAnalyzer):
    """
    Analyzer for VLAN configurations.
    """

    def __init__(self):
        logger.info("Initializing VLANAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze VLAN configurations.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of VLAN-related findings.
        """

        logger.info("Analyzing VLAN configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_vlan_names(parsed_config.vlans)
        )

        findings.extend(
            self._check_unused_vlans(parsed_config.vlans)
        )

        logger.success(
            f"VLAN analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_vlan_names(
        self,
        vlans: list[VLAN],
    ) -> list[Finding]:
        """
        Check VLANs without configured names.
        """

        findings: list[Finding] = []

        for vlan in vlans:

            vlan_name = vlan.name.strip()

            if not vlan_name:

                findings.append(
                    self._create_finding(
                        category="VLAN",
                        severity="Medium",
                        title="Missing VLAN Name",
                        description=(
                            f"VLAN {vlan.vlan_id} does not have a name configured."
                        ),
                        recommendation=(
                            "Configure a meaningful VLAN name."
                        ),
                    )
                )

        return findings

    def _check_unused_vlans(
        self,
        vlans: list[VLAN],
    ) -> list[Finding]:
        """
        Check VLANs with no assigned interfaces.
        """

        findings: list[Finding] = []

        for vlan in vlans:

            interfaces = [
                interface.strip()
                for interface in vlan.interfaces
                if interface.strip()
            ]

            if not interfaces:

                findings.append(
                    self._create_finding(
                        category="VLAN",
                        severity="Low",
                        title="Unused VLAN",
                        description=(
                            f"VLAN {vlan.vlan_id} has no assigned interfaces."
                        ),
                        recommendation=(
                            "Assign interfaces to the VLAN or remove it if unused."
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