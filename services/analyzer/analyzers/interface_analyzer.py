from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, Interface
from utils.logger import logger

class InterfaceAnalyzer(BaseAnalyzer):
    
    """Analyzer for interfcae config
    """
    
    def __init__(self):
        
        logger.info("Initializing InterfaceAnalyzer..")
        
    def analyze(
        self,parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze interface configs
        
        Args:
            Parsed_config: Parsed Cisco config.
            
        Returns:
            List of interface findings.
        """
        logger.info("Analyzing Interfaces")
        
        findings: list[Finding] = []
        
        findings.extend(
            self._check_missing_description(parsed_config.interfaces)
        )
        
        findings.extend(
            self._check_missing_ip(parsed_config.interfaces)
        )
        findings.extend(
            self._check_shutdown(parsed_config.interfaces)
        )
        
        logger.success(f"Interface analysis completed. {len(findings)} finding(s) generated.")
        
        return findings
    
    
    def _check_missing_description(
        self,
        interfaces: list[Interface],
    ) -> list[Finding]:
        
        """Checks for interface without description.
        """
        
        findings: list[Finding] = []
        for interface in interfaces:
            if not interface.description:
                findings.append(
                    Finding(
                        category="Interface",
                        severity="Medium",
                        title="Missing interface description",
                        description=(f"Interface {interface.name} does not have an description."),
                        recommendation=("Configure a meaning full description for the interface")
                    )
                )
        return findings
                

    def _check_missing_ip(
        self,
        interfaces: list[Interface],
    ) -> list[Finding]:
        """
        Check for interfaces without IP addresses.
        """

        findings: list[Finding] = []

        for interface in interfaces:

            if not interface.ip_address:

                findings.append(
                    Finding(
                        category="Interface",
                        severity="High",
                        title="Missing IP Address",
                        description=(
                            f"Interface {interface.name} does not have an IP address configured."
                        ),
                        recommendation=(
                            "Assign an IP address if the interface is expected to participate in Layer 3 routing."
                        ),
                    )
                )

        return findings

    def _check_shutdown(
        self,
        interfaces: list[Interface],
    ) -> list[Finding]:
        """
        Check for administratively shutdown interfaces.
        """

        findings: list[Finding] = []

        for interface in interfaces:

            if interface.shutdown:

                findings.append(
                    Finding(
                        category="Interface",
                        severity="Low",
                        title="Interface Administratively Down",
                        description=(
                            f"Interface {interface.name} is administratively shutdown."
                        ),
                        recommendation=(
                            "Enable the interface if it is expected to be operational."
                        ),
                    )
                )

        return findings
    