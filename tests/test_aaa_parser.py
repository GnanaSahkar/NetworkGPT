
from services.parser.parsers.aaa_parser import AAAParser


def main():

    config = """
aaa new-model

aaa authentication login default group radius local

aaa authorization exec default group radius

aaa accounting exec default start-stop group radius

radius server RADIUS1
 address ipv4 192.168.1.100 auth-port 1812 acct-port 1813

radius server RADIUS2
 address ipv4 192.168.1.101 auth-port 1812 acct-port 1813

tacacs server TACACS1
 address ipv4 192.168.1.200
"""

    parser = AAAParser()

    aaa = parser.parse(config)

    print("\n")
    print("=" * 80)
    print("PARSED AAA CONFIGURATION")
    print("=" * 80)

    print(aaa)


if __name__ == "__main__":
    main()