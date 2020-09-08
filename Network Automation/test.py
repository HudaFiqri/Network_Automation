import paramiko
from netmiko import ConnectHandler

Router_conn = paramiko.SSHClient()

Router_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
Router_conn.connect(hostname='198.18.0.40', port='22', username='user1', password='user1')

stdin, stdout, stderr = Router_conn.exec_command('ip add pri')

out = stdout.readlines()

print(out)

#netmiko


'''
Router = {
    'device_type': 'mikrotik_routeros',
    'host': '198.18.0.40', 
    'username': 'user1', 
    'password':'user1',
}
'''

connect = ConnectHandler(device_type='mikrotik_routeros', host='198.18.0.40', username='user1', password='user1')

output = connect.send_config_set("sys iden set name='RTR_CORE_LINFIQ'")

print(output)