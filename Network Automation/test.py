import netmiko
import Router

#connect module
connect = netmiko.cisco.CiscoIosBase(ip='192.168.1.1', username='administrator', password='administrator123', secret='administrator')
connect.enable()

comm = Router.Cisco.Basic_Configure.Set_Static_Route('192.168.0.1')

#configure module
output = connect.send_config_set("Router_Core")
output2 = connect.send_config_set(comm)

#output
print(output)
print(output2)

#disconnect session
connect.disconnect()
