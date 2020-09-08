#module
import os
import paramiko
import netmiko
import getpass
import Router

#login banner
print('NETWORK AUTOMATION\nCREATE BY LNF LINFIQ 04\n\n\nver0.1.1(beta)\nhelp - show command\n')

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
                password = getpass.getpass('password\n>>> ')

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
