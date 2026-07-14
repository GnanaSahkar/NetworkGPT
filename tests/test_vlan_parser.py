
from services.parser.parsers.vlan_parser import VLANParser

def main():
    
    config = """
vlan 10
 name USERS

vlan 20
 name SERVERS

vlan 30
 name VOICE
"""
    parser = VLANParser()
    vlan = parser.parse(config)
    
    print("\n")
    print("=" * 80)
    print("PARSED VLAN CONFIGURATION")
    print("=" * 80)

    print(vlan)
    
if __name__ == "__main__":
    main()