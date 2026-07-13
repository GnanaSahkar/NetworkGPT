
"""
Data models for NetworkGPT.

Defines the structured objects produced by the
configuration parsers.
"""

from dataclasses import dataclass, field


@dataclass
class Interface:
    """
    Represents a network interface.
    """

    name: str

    description: str = ""

    ip_address: str = ""

    subnet_mask: str = ""

    shutdown: bool = False

    vlan: str = ""

    speed: str = ""

    duplex: str = ""


@dataclass
class AAA:
    """
    Represents AAA configuration.
    """

    authentication: list[str] = field(default_factory=list)

    authorization: list[str] = field(default_factory=list)

    accounting: list[str] = field(default_factory=list)

    radius_servers: list[str] = field(default_factory=list)

    tacacs_servers: list[str] = field(default_factory=list)


@dataclass
class VLAN:
    """
    Represents a VLAN.
    """

    vlan_id: int

    name: str = ""

    interfaces: list[str] = field(default_factory=list)


@dataclass
class OSPF:
    """
    Represents OSPF configuration.
    """

    process_id: int

    router_id: str = ""

    networks: list[str] = field(default_factory=list)

    passive_interfaces: list[str] = field(default_factory=list)


@dataclass
class ACL:
    """
    Represents an Access Control List.
    """

    name: str

    acl_type: str = ""

    entries: list[str] = field(default_factory=list)


@dataclass
class Route:
    """
    Represents a static route.
    """

    destination: str

    subnet_mask: str

    next_hop: str