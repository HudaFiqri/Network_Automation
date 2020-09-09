import netmiko

#connect module
connect = netmiko.cisco.CiscoIosBase(ip='173.10.3.1', username='cperoot', password='nasional123', secret='nasional123')
connect.enable()

#configure module
output = connect.send_config_set('host RTR_CORE')

#output
print(output)

#disconnect session
connect.disconnect()