
"""
Test data models for NetworkGPT.
"""

from services.parser.models import (
    Interface,
    AAA,
    VLAN,
    OSPF,
    ACL,
    Route,
)


def main():

    interface = Interface(
        name="GigabitEthernet0/0",
        description="WAN",
        ip_address="192.168.1.1",
        subnet_mask="255.255.255.0",
        shutdown=False,
    )

    aaa = AAA(
        authentication=[
            "login default group radius local"
        ],
        radius_servers=[
            "192.168.1.100"
        ],
    )

    vlan = VLAN(
        vlan_id=10,
        name="USERS",
    )

    ospf = OSPF(
        process_id=1,
        router_id="1.1.1.1",
    )

    acl = ACL(
        name="ACL-IN",
        acl_type="extended",
    )

    route = Route(
        destination="0.0.0.0",
        subnet_mask="0.0.0.0",
        next_hop="192.168.1.254",
    )

    print("=" * 80)
    print("INTERFACE")
    print(interface)

    print("\n" + "=" * 80)
    print("AAA")
    print(aaa)

    print("\n" + "=" * 80)
    print("VLAN")
    print(vlan)

    print("\n" + "=" * 80)
    print("OSPF")
    print(ospf)

    print("\n" + "=" * 80)
    print("ACL")
    print(acl)

    print("\n" + "=" * 80)
    print("ROUTE")
    print(route)


if __name__ == "__main__":
    main()