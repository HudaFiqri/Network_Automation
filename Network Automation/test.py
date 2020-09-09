import netmiko

connect = netmiko.cisco.CiscoIosBase(ip='173.10.3.1', username='admin', password='Router123')

output = connect.send_command('show users')

print(output)
