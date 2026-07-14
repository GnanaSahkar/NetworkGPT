
from services.parser.parsers.interface_parser import InterfaceParser

def main():
    
    config = """
interface GigabitEthernet0/0
 description WAN Interface
 ip address 192.168.1.1 255.255.255.0
 speed auto
 duplex auto
 no shutdown
    """
    
    parser = InterfaceParser()
    interface = parser.parse(config)
    print("\n")
    print("=" * 80)
    print("PARSED INTERFACE")
    print("=" * 80)
    
    print(interface)

if __name__ == "__main__":
    main()