
from services.parser.parsers.bgp_parser import BGPParser

def main():
    
    config = """
router bgp 65001

 bgp router-id 1.1.1.1

 neighbor 10.10.10.2 remote-as 65002

 neighbor 10.10.20.2 remote-as 65003

 network 192.168.1.0 mask 255.255.255.0
"""
    
    parser = BGPParser()
    bgp = parser.parse(config)
    
    print("\n")
    print("=" * 80)
    print("PARSED BGP CONFIGURATION")
    print("=" * 80)

    print(bgp)    
    
if __name__ == "__main__":
    main()