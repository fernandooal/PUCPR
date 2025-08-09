#!/usr/bin/env python3
import socket
import sys

porta = int(input('Entre com a porta do servidor: '))
ip = input('Entre com o endereço de IP: ')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((ip, porta))
except:
   print('# erro de bind')
   sys.exit()

while True:
    input('Digite <ENTER>')
    data, addr = s.recvfrom(1024)
    print('endereço:', addr, ' enviou:', data)

# s.close() 