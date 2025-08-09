from socket import socket, AF_INET, SOCK_STREAM

HOST = '127.0.0.1'      # localhost = esta máquina
PORT = 9999             # porta usada pela aplicação

s = socket(AF_INET, SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except Exception as e:
    print('erro de bind: ', e)
    exit()

# O parametro do listen é denominado backlog
s.listen(5)


while True:
    print('aguardando conexoes em ', PORT)
    conn, addr = s.accept()

    print('recebi uma conexao de ', addr)
    while True:
        try:
            # O argumento define a quantidade de bytes por leitura
            data = conn.recv(1024) 
            print(f'recebi {len(data)} bytes')

            if not data:
                print('Esta conexao foi encerrada')
                break
            else:
                print(data.decode())

        except Exception as e:
            print('Erro:', e)
            break

