from socket import socket, AF_INET, SOCK_STREAM

HOST = '127.0.0.1'      # localhost = esta máquina
PORT = 9999             # porta usada pela aplicação

PORT = int(input("Entre com a porta do servidor: "))

#STREAM -> TCP
#AF_INET -> IP
#AF_INET6 -> IPv6

s = socket(AF_INET, SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except Exception as e:
    print('erro de bind: ', e)
    exit()

# O parametro do listen é denominado backlog
s.listen(5)

print('aguardando conexoes em ', PORT)

#--------------------------
# insira aqui o codigo para tratar uma conexao
#--------------------------

while True:
    conn, addr = s.accept()
    print('recebi uma conexao de ', addr)
    
    while True:
        try:
            # O argumento define a quantidade de bytes por leitura
            input('Digite <ENTER> para continuar')
            data = conn.recv(1024) 
            print(f'recebi {len(data)} bytes')

            if not data:
                print('Esta conexao foi encerrada')
                break
            else:
                print(data)
        except Exception as e:
            print('Erro:', e)
            break


print('o servidor encerrou')

conn.close() # informa ao cliente que a conexão encerrou
s.close() # informa ao S.O. que a aplicação não quer mais usar a rede