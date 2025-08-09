from socket import socket, AF_INET, SOCK_STREAM

HOST = '127.0.0.1'      # IP do servidor
PORT = 9999             # Porta do servidor         

s = socket(AF_INET, SOCK_STREAM)

try:
    s.connect((HOST, PORT))
    # diferente do servidor, o connect não retorna um outro objeto
    # o socket do cliente é a propria conexão (client-socket)
except Exception as e:
    print('Erro de conexao:', e)
    exit()

while True:
    try:
        data = input('Mensagem: ')
        if not data:
            print('linha vazia encerra o programa')
            break
    
        # encode é usado para coverter de string para bytes
        # string é um objeto python não pode ser enviado pela rede
        tam = s.send(data.encode())          
        print(f'enviei {tam} bytes')

    except Exception as e:
        print('Erro: ', e)
        break