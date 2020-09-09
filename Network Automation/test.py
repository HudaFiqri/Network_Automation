import netmiko

#connect module
connect = netmiko.cisco.CiscoIosBase(ip='192.168.1.1', username='user', password='password', secret='password to priviledge')
connect.enable()

#configure module
output = connect.send_config_set('host RTR_CORE')

#output
print(output)

#disconnect session
connect.disconnect()