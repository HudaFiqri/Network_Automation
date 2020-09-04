#module
import os
import paramiko

os.system('clear')


#login banner
print('CISCO AUTOMATION\nCREATE BY LNF LINFIQ 04\n\n\nhelp - show command\n')

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

                while True:
                    router_command = input('LNF(command-Mikrotik)> ')

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