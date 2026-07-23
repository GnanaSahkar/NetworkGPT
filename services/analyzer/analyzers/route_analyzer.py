"""
Routing configuration analyzer.
"""

from services.analyzer.base_analyzer import BaseAnalyzer
from services.analyzer.models import Finding

from services.parser.models import ParsedConfig, Route

from utils.logger import logger


class RouteAnalyzer(BaseAnalyzer):
    """
    Analyzer for static routing configurations.
    """

    def __init__(self):
        logger.info("Initializing RoutingAnalyzer...")

    def analyze(
        self,
        parsed_config: ParsedConfig,
    ) -> list[Finding]:
        """
        Analyze routing configuration.

        Args:
            parsed_config: Parsed Cisco configuration.

        Returns:
            List of routing-related findings.
        """

        logger.info("Analyzing routing configuration...")

        findings: list[Finding] = []

        findings.extend(
            self._check_default_route(parsed_config.routes)
        )

        findings.extend(
            self._check_duplicate_routes(parsed_config.routes)
        )

        logger.success(
            f"Routing analysis completed. {len(findings)} finding(s) generated."
        )

        return findings

    def _check_default_route(
        self,
        routes: list[Route],
    ) -> list[Finding]:
        """
        Check whether a default route is configured.
        """

        findings: list[Finding] = []

        has_default_route = any(
            route.destination.strip() == "0.0.0.0"
            and route.subnet_mask.strip() == "0.0.0.0"
            for route in routes
        )

        if not has_default_route:

            findings.append(
                self._create_finding(
                    category="Routing",
                    severity="High",
                    title="Missing Default Route",
                    description=(
                        "No default route is configured."
                    ),
                    recommendation=(
                        "Configure a default route to provide connectivity "
                        "to unknown destination networks."
                    ),
                )
            )

        return findings

    def _check_duplicate_routes(
        self,
        routes: list[Route],
    ) -> list[Finding]:
        """
        Check for duplicate static routes.
        """

        findings: list[Finding] = []

        seen_routes: set[tuple[str, str, str]] = set()

        for route in routes:

            route_key = (
                route.destination.strip(),
                route.subnet_mask.strip(),
                route.next_hop.strip(),
            )

            if route_key in seen_routes:

                findings.append(
                    self._create_finding(
                        category="Routing",
                        severity="Medium",
                        title="Duplicate Static Route",
                        description=(
                            f"Duplicate static route detected for "
                            f"{route.destination}/{route.subnet_mask} "
                            f"via {route.next_hop}."
                        ),
                        recommendation=(
                            "Remove duplicate static route entries to simplify "
                            "the routing table."
                        ),
                    )
                )

            else:
                seen_routes.add(route_key)

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