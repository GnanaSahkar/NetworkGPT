from services.parser.parser_service import ParserService
from utils.logger import logger

def main():
    logger.info("Starting ParserService integration test...")

    config = """
hostname R1

!
interface GigabitEthernet0/0
 description WAN Link
 ip address 192.168.1.1 255.255.255.0
 no shutdown

!
interface GigabitEthernet0/1
 description LAN
 ip address 10.0.0.1 255.255.255.0
 shutdown

!
aaa new-model
aaa authentication login default local
aaa authorization exec default local
aaa accounting exec default start-stop group radius
radius server RADIUS1
 address ipv4 192.168.100.10 auth-port 1812 acct-port 1813

!
vlan 10
 name USERS

vlan 20
 name SERVERS

!
router ospf 1
 router-id 1.1.1.1
 network 10.0.0.0 0.0.0.255 area 0
 passive-interface GigabitEthernet0/1

!
ip access-list extended INTERNET-IN
 permit tcp any any eq 80
 permit tcp any any eq 443
 deny ip any any

!
ip route 0.0.0.0 0.0.0.0 192.168.1.254

!
router bgp 65001
 bgp router-id 2.2.2.2
 neighbor 192.168.2.2 remote-as 65002
 network 10.0.0.0 mask 255.255.255.0
"""

    parser_service = ParserService()

    parsed_config = parser_service.parse_config(config)

    logger.success("ParserService integration test completed successfully.")

    print("\n")
    print("=" * 80)
    print("PARSED CONFIGURATION")
    print("=" * 80)

    print(parsed_config)


if __name__ == "__main__":
    main()