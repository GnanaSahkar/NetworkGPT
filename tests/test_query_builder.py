"""
Integration test for QueryBuilder.
"""

from services.parser.parser_service import ParserService
from services.analyzer.analyzer_service import AnalyzerService
from services.ai.query_builder import QueryBuilder

from utils.logger import logger


def print_queries(queries: list[str]) -> None:
    """
    Print generated retrieval queries.
    """

    print("\n" + "=" * 80)
    print("GENERATED RETRIEVAL QUERIES")
    print("=" * 80)

    if not queries:
        print("No queries generated.")
        return

    for index, query in enumerate(queries, start=1):
        print(f"\n{index}. {query}")

    print("\n" + "=" * 80)
    print(f"Total Queries : {len(queries)}")
    print("=" * 80)


def main() -> None:
    """
    Test QueryBuilder.
    """

    logger.info("Starting QueryBuilder integration test...")

    config = """
!
hostname Router1
!
aaa new-model
!
vlan 10
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
!
interface GigabitEthernet0/1
 description LAN Interface
 shutdown
!
ip access-list extended INTERNET
 permit ip any any
!
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
!
router bgp 65001
!
ip route 10.0.0.0 255.255.255.0 192.168.1.1
ip route 10.0.0.0 255.255.255.0 192.168.1.1
!
"""

    # Parse configuration
    parser_service = ParserService()
    parsed_config = parser_service.parse_config(config)

    # Analyze configuration
    analyzer_service = AnalyzerService()
    analysis_report = analyzer_service.analyze(parsed_config)

    # Generate retrieval queries
    query_builder = QueryBuilder()
    queries = query_builder.build_queries(analysis_report)

    # Display queries
    print_queries(queries)


if __name__ == "__main__":
    main()