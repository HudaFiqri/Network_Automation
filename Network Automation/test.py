import netmiko


'''
api = {
    'device_type': 'cisco_ios',
    'host': '173.10.3.1',
    'username': 'cperoot',
    'password': 'nasional123'
}
'''

connect = netmiko.cisco.CiscoIosBase(ip='173.10.3.1', username='cperoot', password='nasional123')

output = connect.send_command('show users')

print(output)
