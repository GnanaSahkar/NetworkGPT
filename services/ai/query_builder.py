"""
Builds RAG retrieval queries from analyzer findings.
"""

from services.analyzer.models import AnalysisReport, Finding
from utils.logger import logger


class QueryBuilder:
    """
    Builds Cisco-specific retrieval queries from an analysis report.
    """
    
    
    QUERY_MAP: dict[str, str] = {
    # AAA
    "missing aaa authentication":
        "Cisco AAA authentication configuration",

    "missing aaa authorization":
        "Cisco AAA authorization configuration",

    "missing aaa accounting":
        "Cisco AAA accounting configuration",

    "no aaa server configured":
        "Cisco RADIUS TACACS+ configuration",

    # Interface
    "missing interface description":
        "Cisco interface description configuration",

    "missing ip address":
        "Cisco interface IP address configuration",

    "interface administratively down":
        "Cisco interface shutdown no shutdown command",

    # VLAN
    "missing vlan name":
        "Cisco VLAN naming best practices",

    "unused vlan":
        "Cisco unused VLAN best practices",

    # OSPF
    "missing ospf router id":
        "Cisco OSPF router-id configuration",

    "no passive interfaces configured":
        "Cisco OSPF passive-interface configuration",

    # ACL
    "overly permissive acl rule":
        "Cisco ACL best practices permit ip any any",

    "empty acl":
        "Cisco ACL configuration",

    # Routing
    "missing default route":
        "Cisco static default route configuration",

    "duplicate static route":
        "Cisco static routing best practices",

    # BGP
    "missing bgp router id":
        "Cisco BGP router-id configuration",

    "no bgp neighbors configured":
        "Cisco BGP neighbor configuration",

    "no advertised bgp networks":
        "Cisco BGP network statement configuration",
    }

    def __init__(self):
        """
        Initialize the QueryBuilder.
        """

        logger.info("Initializing QueryBuilder...")
        logger.success("QueryBuilder initialized.")

    def build_queries(
        self,
        analysis_report: AnalysisReport,
    ) -> list[str]:
        """
        Build unique Cisco documentation retrieval queries.

        Args:
            analysis_report: Analysis report containing findings.

        Returns:
            List of unique retrieval queries.
        """

        logger.info("Building retrieval queries...")

        queries: set[str] = set()

        for finding in analysis_report.findings:

            query = self._build_query(finding)

            if query:
                queries.add(query)

        logger.success(
            f"Generated {len(queries)} retrieval queries."
        )

        return sorted(queries)

    def _build_query(
        self,
        finding: Finding,
    ) -> str:
        """
        Build a Cisco documentation query for a finding.

        Args:
            finding: Analyzer finding.

        Returns:
            Cisco documentation retrieval query.
        """
        """normalized_title = finding.title.strip().lower()
        
        print(f"Finding Title: '{finding.title}'")
        return self.QUERY_MAP.get(
            finding.title,
            f"Cisco {finding.category} configuration","""
            
        normalized_title = finding.title.strip().lower()

        #print(f"Normalized: '{normalized_title}'")
        #print(f"Exists: {normalized_title in self.QUERY_MAP}")

        return self.QUERY_MAP.get(
        normalized_title,
        f"Cisco {finding.category} configuration",
        )