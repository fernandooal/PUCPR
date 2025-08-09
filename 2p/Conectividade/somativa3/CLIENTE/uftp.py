from socket import socket, AF_INET, SOCK_STREAM
import exercicios as EX
import os


#--------------------------------------------------------------------
# Incio do código principal

if __name__ == "__main__":    

    # if os.path.exists("log.txt"): os.remove("log.txt")

    EX.fazLog('INICIO DO TESTE DE UPLOAD\n')

    HOST = '127.0.0.1'          # IP do servidor
    PORT = 9999                 #Porta do servidor
    diretorio = 'TOPSECRET'     

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        EX.fazLog('ERRO: O servidor de FTP não está ativo!!!\n')
        exit()

    if not EX.exercicio1(s, diretorio):
        EX.exercicio2(s,diretorio)
    else:
        EX.exercicio3(s,diretorio)
               
    while True:
        arquivo = input('Digite o nome do arquivo para transferir: ')
        if not arquivo:
            print('O usuário desistiu')
            exit()
        if EX.exercicio4(arquivo):
            break
        else:
            EX.fazLog(f'O arquivo {arquivo} nao existe\n')
    
#---------------------------------------------------------------------------------------------

    s2 = socket(AF_INET, SOCK_STREAM)
    try:
        s2.bind(('', 9998))
        s2.listen(1)
    except:
        EX.fazLog('ERRO: a porta 9998 está sendo usada\n')
        exit()

    # Envia ordem de upload ao servidor
    path = os.path.join(diretorio, arquivo)
    comando = f'upload({path})\n'
    s.send(comando.encode())
    EX.fazLog(f'O cliente enviou {comando}\n')

    # Aguarda a conexão para criaro canal de dados
    conn, addr = s2.accept()
    EX.fazLog(f'Servidor {addr} fez a conexao\n')

    # Chama a função que transfere arquivo pelo canal de dados

    try:
        EX.exercicio5(conn, arquivo)
        EX.fazLog('O arquivo foi transferido\n')
        input('Digite <ENTER> para encerrar')
    except Exception as e:
        EX.fazLog(f'O upload falhou: {e}')

    conn.close()
    s2.close()

    EX.fazLog('FIM DO TESTE DE UPLOAD\n')