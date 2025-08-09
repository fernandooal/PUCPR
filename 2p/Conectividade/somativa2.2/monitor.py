#!/usr/bin/env python3
import socket
import sys
import threading

#--------------------------------------------------------------
# FUNÇÕES

def TrataSensor(conn, addr):

  print('Uma thread foi criada para:', addr)

  # O sensor deve enviar seu ID apos a conexao
  sensor = conn.recv(10)
  SENSORES[sensor] = conn

  print('sensor ', sensor, ' registrado no socket', conn) 
 
  while True:
    try:
        data = conn.recv(100)
        print('sensor ', sensor, 'enviou ', data)

        if not data:
            print("O dispositivo de IoT enviou FINISH")
            break
    except Exception as e:
        print("O dispositivo de IoT enviou um RESET")
        break
       
  conn.close()     
  print('O sensor', sensor, 'encerrou')

#--------------------------------------------------------------
# PROGRAMA PRINCIPAL

HOST = ''               # ANY_IP = todos os IPs do HOST
SENSORES={}     # lista de sensores conectados
CONSOLE=None  # conexao com o console remoto

PORTA = int(input('Entre com a porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORTA))
except:
   print('# erro de bind')
   sys.exit()

s.listen(2) # BACKLOG

print('aguardando conexoes em ', PORTA)

#--------------------------------------------------------------
# LOOP para tratar clientes

while True:
    conn, addr = s.accept()
    print('recebi uma conexao do sensor ', addr)

    t = threading.Thread( target=TrataSensor, args=(conn,addr,))
    t.start()
#--------------------------------------------------------------

print('o servidor encerrou')
s.close()