

from services.parser.parsers.route_parser import RoutingParser

def main():
    config = """
ip route 0.0.0.0 0.0.0.0 192.168.1.1

ip route 10.10.10.0 255.255.255.0 172.16.1.1
"""
    parser = RoutingParser()
    route = parser.parse(config)
    
    print("\n")
    print("=" * 80)
    print("PARSED ROUTING CONFIGURATION")
    print("=" * 80)

    print(route)
    
if __name__ == "__main__":
    main()