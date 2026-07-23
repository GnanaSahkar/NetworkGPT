"""
Analyzer service.
"""

from services.analyzer.analyzers.aaa_analyzer import AAAAnalyzer
from services.analyzer.analyzers.acl_analyzer import ACLAnalyzer
from services.analyzer.analyzers.bgp_analyzer import BGPAnalyzer
from services.analyzer.analyzers.interface_analyzer import InterfaceAnalyzer
from services.analyzer.analyzers.ospf_analyzer import OSPFAnalyzer
from services.analyzer.analyzers.route_analyzer import RouteAnalyzer
from services.analyzer.analyzers.vlan_analyzer import VLANAnalyzer

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import AnalysisReport

from services.parser.models import ParsedConfig

from utils.logger import logger


class AnalyzerService:
    """
    Service responsible for orchestrating all configuration analyzers.
    """

    def __init__(self):
        """
        Initialize the analyzer service.
        """

        logger.info("Initializing AnalyzerService...")

        self.analyzers: list[BaseAnalyzer] = [
            InterfaceAnalyzer(),
            VLANAnalyzer(),
            ACLAnalyzer(),
            AAAAnalyzer(),
            OSPFAnalyzer(),
            RouteAnalyzer(),
            BGPAnalyzer(),
        ]

        logger.success(
            f"AnalyzerService initialized with "
            f"{len(self.analyzers)} analyzers."
        )

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> AnalysisReport:
        """
        Analyze a parsed configuration.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            AnalysisReport containing all findings.
        """

        logger.info("Starting configuration analysis...")

        findings = []

        for analyzer in self.analyzers:

            logger.info(
                f"Running {analyzer.__class__.__name__}..."
            )

            findings.extend(
                analyzer.analyze(parsed_config)
            )

        logger.success(
            f"Configuration analysis completed. "
            f"Generated {len(findings)} finding(s)."
        )

        return AnalysisReport(
            findings=findings,
        )