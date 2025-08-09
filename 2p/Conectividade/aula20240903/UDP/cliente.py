#!/usr/bin/env python3
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input('Entre com o IP de destino: ')
porta = int(input('Entre com a porta de destino: '))
    
s.setblocking(0)
while True:
    msg = input('Entre com a mensagem: ')
    s.sendto(msg.encode(), (ip, porta))
    time.sleep(1)
    try:
        data, addr = s.recvfrom(1024) 
        print(data)   
    except:
        print('O servidor não confirmou')


# s.close()