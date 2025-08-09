#!/usr/bin/env python3
import socket
import sys

porta = int(input('Entre com a porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind(('', porta))
except:
   print('# erro de bind')
   sys.exit()
    
while True:
    try:
        data, addr = s.recvfrom(1000)
        print('sensor ', addr, ' enviou:', data)
        s.sendto("ACK".encode(), addr)
    except Exception as e:
        print(e)
        print('Recebi uma mensagem muito grande')

# s.close()