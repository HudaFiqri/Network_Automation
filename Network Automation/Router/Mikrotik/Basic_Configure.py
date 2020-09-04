#set basic configure for router can access internet
def Set_Basic_Access(internet_port=None):
    '''
    set port for internet access and automation dhcp client
    '''
    access_internet = 'ip dhcp-client add interface='+ internet_port + ' disable=no\n'+ 'chain=srcnat action=masquerade out-interface='+ internet_port
    return access_internet
    
#set router hostname
def Set_Hostname(name=None):
    '''
    set name for change your mikrotik hostname
    '''
    Set_Hostname = 'system identity set name='+ name
    return Set_Hostname

#set local username
def Set_User(name=None, group=None):
    '''
    basic configuration for local users on mikrotik.
    users on Mikrotik use several types, namely: full (full access), 
    read (read only), and write (only write)
    '''
    user_name =('name = '+ name + ' ' + 'group = '+ group)
    return user_name

#set default routing static
def Set_Static_Route(address=None, password=None, gateway=None):
    '''
    for address must using network and prefix example 192.168.0.0/24 and gateway ip host
    example 192.168.1.1
    '''
    static_route =('dst-address='+ address + ' '+ 'password=' + password+ ' ' + 'gateway= '+ gateway)
    return static_route

comm1 = 'user1'
comm2 = 'full'
comm3 = 'user1'
test = Set_Static_Route(address=comm1, password=comm3, gateway=comm2)
print(test)