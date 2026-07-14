
from services.parser.parsers.ospf_parser import OSPFParser

def main():
    
    config = """
router ospf 1

 router-id 1.1.1.1

 network 10.0.0.0 0.0.0.255 area 0

 passive-interface GigabitEthernet0/1
"""
    
    parser = OSPFParser()
    ospf = parser.parse(config)
    
    print("\n")
    print("=" * 80)
    print("PARSED OSPF CONFIGURATION")
    print("=" * 80)

    print(ospf)
    
if __name__ == "__main__":
    main()