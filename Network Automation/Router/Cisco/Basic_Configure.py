#set client interface
def Set_Interface_Client(interface="", address=""):
    """
    configure for client to get gateway
    """
    Client = (
        "interface "+ interface +
        "\nip address "+ address +
        "\nexit\n"
    )
    return Client

#set dhcp server
def Set_DHCP_Server(name="", network="", gateway="", dns=""):
    """
    configure dhcp server for client to get dynamic ip address
    """
    DHCP_Server = (
        "ip dhcp pool "+ name +
        "\ndefault-router "+ gateway +
        "\ndns "+ dns+
        "\nexit\n"
    )
    return DHCP_Server

#configure NAT to access internet
def Set_Basic_Access(WAN_interface="", LAN_interface=""):
    """
    configure this for client can access internet
    """
    Basic_Configure = Set_Basic_Access(
        "ip access-list extended CLIENT"+
        "\npermit ip any any"+
        "\nexit"+
        "\ninterface "+ WAN_interface +
        "\ninterface "+ LAN_interface +
        "\nip nat inside source list CLIENT interface"+ WAN_interface +"overload"
    )
    return Basic_Configure

WAN = 'gigabyte 0/0'
LAN = 'gigabyte 0/1'


output = Set_Basic_Access(WAN, LAN)
print(output)