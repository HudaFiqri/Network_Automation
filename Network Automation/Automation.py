#module
import os
import paramiko
import getpass
import Router

os.system('clear')


#login banner
print('NETWORK AUTOMATION\nCREATE BY LNF LINFIQ 04\n\n\nver0.0.1(alpha)\nhelp - show command\n')

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
                print('clear - clear screen')
                print('help - show command')
                print('mikrotik - connecting with the type of the Mikrotik brand')
                print('\n')

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
                #stdin, stdout, stderr = Router_API.exec_command(router_command)
                #Router_run_command = stdout.readlines()
                #print(Router_run_command)

                while True:
                    print('\n')
                    router_command = input('LNF(command-Mikrotik)> ')

                    

                    if(router_command == 'end'):
                        break

                    elif(router_command == 'help'):
                        print('mikrotik')
                        print('basic_command - configure basic command for mikrotik access internet')
                        print('clear - clear screen')
                        print('end - back')
                        print('help - show command')
                        print('\n')

                    elif(router_command == 'basic_command'):

                        os.system('clear')

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

                            Router_Command_Call = stdout.readlines()

                        elif(choice_next == 'y'):
                            continue

                        else:
                            print('command error')

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
