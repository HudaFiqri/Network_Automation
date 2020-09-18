#module
import os
import paramiko
import netmiko
import getpass
import Router

#login banner
print('NETWORK AUTOMATION\nCREATE BY LNF LINFIQ 04\n\n\nver0.2.1\nhelp - show command\n')

while True:

    #input
    input_command = input('LNF(automation) > ')

    #input command
    if(input_command == 'help'):
        print('\n')
        print('exit - exit program')
        print('help - show command')
        print('ssh - connect devices using SSH')
        print('\n')

    #ssh command
    elif(input_command == 'ssh'):
        
        while True:

            #input shh
            ssh_command = input('LNF(SSH)> ')

            if(ssh_command == 'help'):
                print('\n')
                print('cisco - connecting with the type of the Cisco brand')
                print('back - back to menu')
                print('help - show command')
                print('mikrotik - connecting with the type of the Mikrotik brand')
                print('\n')

            #cisco brand
            elif(ssh_command == 'cisco'):
                hostname = input('hostname address\n>>> ')
                port = input('port\n>>> ')
                username = input('username\n>>> ')
                password = input('password\n>>> ')
                secret = input('insert secret your cisco device\n>>> ')

                #connect module
                Router_API = netmiko.cisco.CiscoIosBase(ip=hostname, username=username, password=password, secret=secret)
                Router_API.enable()
                while True:
                    router_command = input('LNF(command-Cisco)> ')

                    if(router_command == "help"):
                        print('\n')
                        print('help - show command')
                        print('exit - stop connection')
                        print('route - set static route for router to access network')
                        print('internet - set nat so that clients can access the internets')
                        print('dhcp - set dhcp server so that clients get automatic ip address')
                        print('\n')

                    elif(router_command == 'dhcp'):

                        #command for setting
                        Pool_Name = input("set pool name\n>>> ")
                        network_address = input("set network address and subnet example[192.168.0.0 255.255.255.0]\n>>> ")
                        gateway_address = input('set gateway address\n>>> ')
                        dns_address = input('set dns address\n>>> ')

                        #setting module
                        Set_DHCP_Server = Router.Cisco.Set_DHCP_Server(name="",network="", gateway="", dns="")
                        Set_DHCP = Router_API.send_config_set(Set_DHCP_Server)
                        print(Set_DHCP)

                    elif(router_command == 'internet'):
                        Set_Internet_Port = input("enter your port of ethernet\n>>> ")
                        Set_Local_Port = input("enter your port of local connection\n>>> ")
                        Set_Internet_Access = Router.Cisco.Set_Basic_Access(internet_port=Set_Internet_Port, local_port=Set_Local_Port)
                        Set_Internet_Output = Router_API.send_config_set(Set_Internet_Access)
                        print(Set_Internet_Output)

                    elif(router_command == "route"):
                        Router_Gateway = input('gateway\n>>> ')
                        Static = Router.Cisco.Set_Static_Route(gateway=Router_Gateway)
                        output = Router_API.send_config_set(Static)
                        print(output)

                    elif(router_command == "exit"):
                        break

                    else:
                        print("\ncommand error\n")

            #mikrotik brand
            elif(ssh_command == 'mikrotik'):
                hostname = input('hostname address\n>>> ')
                port = input('port\n>>> ')
                username = input('username\n>>> ')
                password = getpass.getpass('password\n>>> ')

                #connect module
                Router_API = paramiko.SSHClient()
                Router_API.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                Router_API.connect(hostname, port, username, password)
                while True:
                    print('\n')
                    router_command = input('LNF(command-Mikrotik)> ')

                    if(router_command == 'end'):
                        break

                    elif(router_command == 'help'):
                        print('\n')
                        print('default - configure basic command for mikrotik access internet')
                        print('forward - configure port forwarding for change destination port')
                        print('limit - configure bandwidth limitation per user')
                        print('end - back')
                        print('help - show command')
                        print('\n')

                    elif(router_command == 'forward'):
                        destination_address = input('set destination address\n>>> ')
                        source_port = input('set source port\n>>> ')
                        destination_port = input('set destination port\n>>> ')
                        protocol = input('set protocol type\n>>> ')
                        internet_access = input('set interface to destination interface\n>>> ')

                        Set_Port_Forwarding = Router.Mikrotik.Set_Port_Forwarding(destination_address, source_port, destination_port, protocol, internet_access)

                        stdin, stdout, stderr = Router_API.exec_command(Set_Port_Forwarding)

                        stdout.readlines()

                    elif(router_command == 'limit'):
                        name_queue = input('set name queue\n>>> ')
                        address = input('set address device\n>>> ')
                        download_max = input('set max download byte example 256k\n>>> ')
                        upload_max = input('set max upload byte example 256k\n>>> ')

                        Set_Simple_Queue = Router.Mikrotik.Set_Simple_Queue(name_queue, address, upload_max, download_max)

                        stdin, stdout, stderr = Router_API.exec_command(Set_Simple_Queue)
                        stdout.readlines()

                    elif(router_command == 'default'):

                        #command for setting
                        internet_port = input('set internet port on your router example ether1\n>>> ')
                        hostname_router = input('\nset hostname on your router\n>>> ')
                        user_name = input('\nset user local for your router\n>>> ')
                        user_pass = input('set password for your user\n>>> ')
                        user_type = input('set the user type for your user(full, read, write)\n>>> ')
                        choice_next = input('\nwhat is your router uses the dhcp client? y/n\n>>> ')

                        #for calling package
                        Basic_Setting_internet = Router.Mikrotik.Basic_Configure.Set_Basic_Access(internet_port)
                        Basic_Setting_hostname = Router.Mikrotik.Basic_Configure.Set_Hostname(hostname_router)
                        Basic_Setting_user = Router.Mikrotik.Basic_Configure.Set_User(user_name, user_pass, user_type)

                        stdin, stdout, stderr = Router_API.exec_command(Basic_Setting_internet + '\n' + Basic_Setting_hostname + '\n' + Basic_Setting_user)
                        Router_Command_Call = stdout.readlines()

                        if(choice_next == 'n'):
                            network_address = input('insert your network address\n>>> ')
                            gateway_address = input('insert your gateway address\n>>> ')
                            Basic_Setting_Static_Router = Router.Mikrotik.Basic_Configure.Set_Static_Route(network_address, gateway_address)

                            stdin, stdout, stderr = Router_API.exec_command(Basic_Setting_Static_Router)

                            stdout.readlines()

                        elif(choice_next == 'y'):
                            continue

                        else:
                            print('command error')

                    else:
                        print('command error')

            elif(ssh_command == 'back'):
                break

            else:
                print('\n')
                print('command error')
                print('\n')

    elif(input_command == 'exit'):
        exit()

    else:
        print('\n')
        print('command error')
        print('\n')
