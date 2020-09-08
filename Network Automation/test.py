from netmiko import mikrotik

host = '192.168.43.16'
user = 'user1'
passw = 'user1'
command = input('>>> ')

api = mikrotik.MikrotikRouterOsSSH(
    host='192.168.43.16',
    username='user1',
    password='user1',
    device_type='mikrotik',
    encoding=ascii
)

api.send_command('ip address print')
