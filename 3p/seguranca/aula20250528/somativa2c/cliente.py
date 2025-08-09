import socket
import ssl

host_addr = '127.0.0.1'
host_port = 40232
peer_name = 'server.bcc.com'
peer_cert = 'bcc_CA.crt'
my_cert = 'client.crt'
my_key = 'client.key'

def prepara_contexto():
    contexto = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    contexto.verify_mode = ssl.CERT_REQUIRED
    contexto.load_cert_chain(certfile=my_cert, keyfile=my_key)
    contexto.load_verify_locations(cafile=peer_cert)
    contexto.check_hostname = False # mudar para True no TDE
    return contexto

def verifica_conexao(ssock):
    print('cipher selecionado: ', ssock.cipher())

    cert = ssock.getpeercert()
    
    for i in cert['subject']: 
        if i[0][0] == 'commonName': identidade = i[0][1]
    for i in cert['issuer']: 
        if i[0][0] == 'commonName': issuer = i[0][1]
        
    print(f'Recebi o certificado de {identidade} emitido por {issuer}')
        
    return identidade

def faz_conexao(s, contexto):
    try:
        ssock = contexto.wrap_socket(s, server_side=False, server_hostname=peer_name)
        ssock.connect((host_addr, host_port))
        sid = verifica_conexao(ssock)

        return ssock, sid

    except Exception as e:
        print(e)
        return None, 'LIAR!!!'
    
if __name__ == "__main__":

    contexto = prepara_contexto() 

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        ssock, sid = faz_conexao(s, contexto)
        if ssock is None: exit()           
        
        print(f'Conectado em {sid}')

        ssock.settimeout(1)
        while True:
            try:
                data = ssock.recv()
                if not data: break
                else: print( 'MENSAGEM DO SERVIDOR: ', data.decode() )
            except socket.timeout:
                msg = input('mensagem: (ou <ENTER> para encerrar): ')
                if not msg: break           
                ssock.send(msg.encode())

            except Exception as e:
                print('A conexão caiu: ', e)
                break


        ssock.close()