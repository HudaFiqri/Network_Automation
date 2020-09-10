import netmiko
import Router

#connect module
connect = netmiko.cisco.CiscoIosBase(ip='173.10.3.1', username='cperoot', password='nasional123', secret='nasional123')
connect.enable()

comm = Router.Cisco.Basic_Configure.Set_Static_Route('123.2.3.1')

#configure module
output = connect.send_config_set("host LNX")
output2 = connect.send_config_set(comm)

#output
print(output)
print(output2)

#disconnect session
connect.disconnect()