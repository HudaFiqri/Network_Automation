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
        "\nnetwork "+ network+
        "\ndns "+ dns+
        "\nexit\n"
    )
    return DHCP_Server

#configure NAT to access internet
def Set_Basic_Access(internet_port="", local_port=""):
    '''
    set basic configure for client can connect to internet
    '''
    Set_Access =(
        "interface "+ internet_port +
        "\nip nat out" +
        "\nexit"
        "\ninterface "+ local_port +
        "\nip nat in" +
        "\nexit" +
        "\nip access-list extended CLIENT" +
        "\npermit ip any any" +
        "\nexit"
        "\nip nat inside source list CLIENT interface "+ internet_port +" overload"
    )
    return Set_Access

#set default routing static
def Set_Static_Route(gateway=""):
    """
    configure static route
    """
    Static_Route = (
        "ip route 0.0.0.0 0.0.0.0 "+ gateway
    )
    return Static_Route
