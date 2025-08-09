#!/usr/bin/python3

import socket
import ssl
from threading import Thread

server_ip = '127.0.0.1'
server_port = 40232
my_cert = 'server.crt'
my_key = 'server.key'
peer_cert = 'bcc_CA.crt'

def prepara_contexto():
    contexto = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    contexto.verify_mode = ssl.CERT_REQUIRED
    contexto.load_cert_chain(certfile=my_cert, keyfile=my_key)
    contexto.load_verify_locations(cafile=peer_cert)
    return contexto

def verifica_conexao(ssock):
    ciphers = ssock.shared_ciphers()
    if ciphers is not None:
        print('ciphers negociados: ')
        for c in ssock.shared_ciphers(): print(c)
    
    print('Cipher selecionado: ', ssock.cipher())

    cert = ssock.getpeercert()

    for i in cert['subject']: 
        if i[0][0] == 'commonName': identidade = i[0][1]
    for i in cert['issuer']: 
        if i[0][0] == 'commonName': issuer = i[0][1]

    print(f'Recebi o certificado de {identidade} emitido por {issuer}')
    
    return identidade

def recebe_conexao(s, contexto):
    cid='desconhecido'
    (csock, caddr) = s.accept()

    try:
        ssock = contexto.wrap_socket(csock, server_side=True)
        cid = verifica_conexao(ssock)

        ssock.send(f'OLA {cid} bem vindo ao servidor TLS\n'.encode())

        return ssock, cid

    except Exception as e:
        print(e)
        return None, 'LIAR!!!'
    
def trata_cliente(ssock, cid):  
    try:
        while True:
            data = ssock.recv(4096)
            if not data: break
            else: ssock.send(f'Prezado {cid}, recebi sua mensagem de {len(data)} bytes'.encode())
    except Exception as e:
        print(e)
    finally:
        print(f'O cliente {cid} encerrou')
        ssock.shutdown(socket.SHUT_RDWR)
        ssock.close()

if __name__ == "__main__":

    contexto = prepara_contexto()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((server_ip, server_port))
        s.listen(5)

        while True:
            print("Aguardando clientes")
            ssock,cid = recebe_conexao(s, contexto)
            if ssock is not None:
                t = Thread(target=trata_cliente, args=(ssock,cid))
                t.start()
            else:
                print('Uma conexão ilegal foi bloqueada')

