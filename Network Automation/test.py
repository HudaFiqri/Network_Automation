'''
simple:
- basic internet configure
- limit upload download device
- port forwarding

advance
- bridge
- routing
- system
- upgrade and downgrade
- backup and restore system
'''

import Router

name_queue = input('set name queue\n>>> ')
address = input('set address device\n>>> ')
download_max = input('set max download byte example 256k\n>>> ')
upload_max = input('set max upload byte example 256k\n>>> ')

Set_Simple_Queue = Router.Mikrotik.Set_Simple_Queue(name_queue, address, upload_max, download_max)