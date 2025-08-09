from socket import socket, AF_INET, SOCK_STREAM
import exercicios as EX
import time
import os
import ast


def Download(path, conn):
    # Obtenha o nome do arquivo a partir do path
    file = EX.exercicio9(path)
    # Abrir o arquivo em modo escrita
    try:
        EX.exercicio10(conn, file)
    except Exception as e:
        EX.fazLog(f'ERRO {e}\n')
    
def selPastaLocal():

    EX.exercicio6()

    dir = input('Selecione ou crie a pasta de Download: ')
    if len(dir) > 0:
        EX.exercicio7(dir)
    
    EX.fazLog(f'Pasta Download: {os.getcwd()}\n')
  
def arquivoRemoto(s):
    # Lista o diretorio no servidor remoto
    s.send('os.listdir()\n'.encode())
    time.sleep(1) #essa espera é para receber a resposta completa sem ter que criarum while
    resposta = s.recv(2048).decode()
    EX.fazLog(f'Conteudo remoto: {resposta}\n')

    # Seleciona um subdiretório
    dir = input('Digite a pasta de Upload (Remota) ou <ENTER> para manter a mesma: ')
    
    if len(dir) > 0:
        if dir not in eval(resposta):
            print('Esse diretorio não pode ser selecionado')
        else:
            s.send(f'os.listdir({dir})\n'.encode())            
            time.sleep(2) 
            resposta = s.recv(2048).decode()
            EX.fazLog(f'Conteudo remoto: {resposta}\n')

    try:
        arquivos = ast.literal_eval(resposta)
    except:
        EX.fazLog(resposta)
        exit()
        
    while True:
        file = input('Selecione o arquivo para download: ')
        if not file:
            EX.fazLog('O usuario desistiu\n')
            exit()
        if file not in arquivos:
            EX.fazLog(f'O arquivo {file} nao existe\n')
        else:
            break

    # Retorna o caminho para um arquivo da lista 
    return EX.exercicio8(dir, file)



#--------------------------------------------------------------------
# Incio do código principal

if __name__ == "__main__":    

    EX.fazLog('INICIO DO TESTE DE DONWLOAD\n')

    HOST = '127.0.0.1'          # IP do servidor
    PORT = 9999                 #Porta do servidor

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        EX.fazLog('ERRO: O servidor de FTP não está ativo!!!\n')
        exit()

    print('selecao da pasta local ...')
    selPastaLocal()

    print('selecao do arquivo remoto ...')
    remoto = arquivoRemoto(s)

    if not remoto:
        EX.fazLog('O arquivo remoto não foi selecionado. Bye!!!\n')
        exit()

    print(remoto)

    s2 = socket(AF_INET, SOCK_STREAM)
    try:
        s2.bind(('', 9998))
        s2.listen(1)
    except:
        EX.fazLog('ERRO: a porta 9998 está ocupada')
        exit()

    # Envia ordem de download ao servidor
    s.send(f'download({remoto})\n'.encode())

    # Aguarda a conexão para criaro canal de dados
    conn, addr = s2.accept()
    EX.fazLog(f'Servidor {addr} fez a conexao\n')

    # Chamada para rotina de download
    try:
        Download(remoto, conn)
        EX.fazLog('O arquivo foi transferido\n')
    except Exception as e:
        EX.fazLog('ERRO DE DOWNLOAD: {e}\n')

    EX.fazLog(f'PASTA {os.getcwd()}: {os.listdir()}\n')
    s.close()
    input('Digite <ENTER> para encerrar')
    EX.fazLog('FIM DO TESTE DE DONWLOAD\n')
