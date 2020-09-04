#module
import os
import paramiko
import getpass
from Router import Mikrotik

os.system('clear')


#login banner
print('NETWORK AUTOMATION\nCREATE BY LNF LINFIQ 04\n\n\nver1.0(beta)\nhelp - show command\n')

while True:

    #input
    input_command = input('LNF(automation) > ')

    #input command
    if(input_command == 'help'):
        print('\n')
        print('clear - clear screen')
        print('exit - exit program')
        print('help - show command')
        print('ssh - connect devices using SSH')
        print('telnet - connect devices using telnet')
        print('\n')

    #ssh command
    elif(input_command == 'ssh'):

        os.system('clear')
        
        while True:

            #input shh
            ssh_command = input('LNF(SSH)> ')

            if(ssh_command == 'help'):
                print('\n')
                print('back - back to menu')
                print('cisco - connecting with the type of the Cisco brand')
                print('clear - clear screen')
                print('forti - connecting with the type of the Forti brand')
                print('help - show command')
                print('mikrotik - connecting with the type of the Mikrotik brand')
                print('\n')

            #mikrotik brand
            elif(ssh_command == 'mikrotik'):
                hostname = input('hostname address\n>>> ')
                port = input('port\n>>> ')
                username = input('username\n>>> ')
                password = input('password\n>>> ')

                #connect module
                Router_API = paramiko.SSHClient()
                Router_API.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                Router_API.connect(hostname, port, username, password)
                #stdin, stdout, stderr = Router_API.exec_command(router_command)
                #Router_run_command = stdout.readlines()
                #print(Router_run_command)

                while True:
                    router_command = input('LNF(command-Mikrotik)> ')

                    

                    if(router_command == 'end'):
                        break

                    elif(router_command == 'help'):
                        print('basic_command - configure basic command for mikrotik access internet')
                        print('clear - clear screen')
                        print('end - back')
                        print('help - show command')
                        print('\n')

                    elif(router_command == 'basic_command'):

                        os.system('clear')

                        #command for setting
                        print('\nfill "ether1" if your router using port 1 for internet access\n')
                        internet_port = input('insert internet port on your router\n>>> ')
                        print('\n\ngive your router a name\n')
                        hostname_router = input('insert hostname on your router\n>>> ')
                        print('\n\nadd user for your router\n')
                        user_name = input('add user on your router\n>>> ')
                        user_pass = getpass.getpass('add password for your user\n>>> ')
                        user_type = input('\nset the user type for your user(full, read, write)\n>>> ')
                        choice_next = input('\nwhat is your router uses the dhcp client? y/n\n>>> ')

                        #for calling package
                        Basic_Setting_internet = Mikrotik.Basic_Configure.Set_Basic_Access(internet_port)
                        Basic_Setting_hostname = Mikrotik.Basic_Configure.Set_Hostname(hostname_router)
                        Basic_Setting_user = Mikrotik.Basic_Configure.Set_User(user_name, user_pass, user_type)

                        stdin, stdout, stderr = Router_API.exec_command(Basic_Setting_internet + '\n' + Basic_Setting_hostname + '\n' + Basic_Setting_user)
                        Router_Command_Call = stdout.readlines()

                        if(choice_next == 'n'):
                            network_address = input('insert your network address\n>>> ')
                            gateway_address = input('insert your gateway address\n>>> ')
                            Basic_Setting_Static_Router = Mikrotik.Basic_Configure.Set_Static_Route(network_address, gateway_address)

                            stdin, stdout, stderr = Router_API.exec_command(Basic_Setting_Static_Router)

                            Router_Command_Call = stdout.readlines()

                        elif(choice_next == 'y'):
                            continue

                        else:
                            print('command error')

                    else:
                        print('command error')



            #cisco brand
            elif(ssh_command == 'cisco'):
                hostname = input('hostname address\n>>> ')
                port = input('port\n>>> ')
                username = input('username\n>>> ')
                password = input('password\n>>> ')

                while True:
                    router_command = input('LNF(command-Cisco)> ')

                    #connect module
                    Router_API = paramiko.SSHClient()
                    Router_API.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    Router_API.connect(hostname, port, username, password)
                    stdin, stdout, stderr = Router_API.exec_command(router_command)
                    Router_run_command = stdout.readlines()
                    print(Router_run_command)

                    if(router_command == 'exit'):
                        break
                    else:
                        print('command error')

            elif(ssh_command == 'forti'):
                hostname = input('hostname address\n>>> ')
                port = input('port\n>>> ')
                username = input('username\n>>> ')
                password = input('password\n>>> ')

                while True:
                    router_command = input('LNF(command-Forti)> ')

                    #connect module
                    Router_API = paramiko.SSHClient()
                    Router_API.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    Router_API.connect(hostname, port, username, password)
                    stdin, stdout, stderr = Router_API.exec_command(router_command)
                    Router_run_command = stdout.readlines()
                    print(Router_run_command)

                    if(router_command == 'exit'):
                        break
                    else:
                        print('command error')

            elif(ssh_command == 'clear'):
                os.system('clear')

            elif(ssh_command == 'back'):
                break

            else:
                print('\n')
                print('command error')
                print('\n')


    elif(input_command == 'clear'):
        os.system('clear')

    elif(input_command == 'exit'):
        exit()

    else:
        print('\n')
        print('command error')
        print('\n')
