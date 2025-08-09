from socket import socket
from datetime import datetime
import time
from ast import literal_eval
import os

def fazLog(msg: str):
    '''
    Registra em um log a mensagem recebida
    - Não altere essa função
    - O arquivo log.txt deve sem entregue como resultado da tarefa
    - O log é único para cada equipe pois inclui portas aleatórias e horário de cada evento     
    '''

    pydir=  os.path.dirname(os.path.realpath(__file__))

    print(msg, end='')
    f = open(os.path.join(pydir,'log.txt'), 'a')
    f.write(f'{datetime.now()} : {msg}')
    f.close()


def exercicio1(s:socket, dir:str) -> bool:
    '''
    Verifica se o diretório existe no servidor remoto

    Parametros:
    - s: socket tcp que representa a conexao o servidor remoto
    - dir: diretório que será pesquisado

    Retorna: True se a pasta existir, Fase caso contrário
    '''

    # DICAS:  
    # Substitua COMANDO pelo comando da biblioteca os que lista os arquivos do diretório corrente
            
    comando = f'os.listdir()\n'

    #---------------- NAO ALTERE A PARTIR DAQUI ----------------------------

    s.send(comando.encode())
    time.sleep(1)
    resultado = s.recv(4096).decode()
    fazLog(f'Pasta raiz do servidor remoto: {resultado}')

    try:
        resposta = literal_eval(resultado) # converte a string para um objeto python de forma segura
    except:
        resposta = resultado

    if type(resposta) != list:
        fazLog('Esqueci de fazer o Exercicio 1\n')

    if dir not in resposta:
        return False
    else:
        return True

def exercicio2(s:socket, dir:str):
    '''
    Cria uma pasta no servidor remoto

    Parametros:
    - s: socket tcp que representa a conexao o servidor remoto
    - dir: diretório quer será criada
    '''

    # DICAS: 
    # monte a string com o comando f'os.COMMANDO({dir})\n'. Pesquise qual o COMANDO que cria um diretório
    # use a sequencia de comandos do exercicio1 para transmitir o comando, aguardar 1 segundo para pegar o resultado
    # salve o resultado como string na variavel resultado. Não use ast_literal.

    comando = f'os.makedirs({dir})\n'
    s.send(comando.encode())
    time.sleep(1)
    resultado = s.recv(4096).decode()

    #---------------- NAO ALTERE A PARTIR DAQUI ----------------------------
        
    fazLog(f'Criacao da pasta remota: {resultado}')

    

def exercicio3(s:socket, dir:str) -> list:
    '''
    Lista o conteúdo de uma diretório no servidor remoto

    Parametros:
    - s: socket tcp que representa a conexao o servidor remoto
    - dir: diretório quer será pesquisado
    '''

    # DICAS: 
    # monte a string com f'os.COMMANDO({dir})\n'. Pesquise qual o COMANDO que permite listar diretorios
    # transmita o comando para o servidor e aguarde um segundo para pegar o resultado.
    # salve o resultado como string na variavel resultado. Não use ast_literal.
    
    comando = f'os.listdir({dir})\n'
    s.send(comando.encode())
    time.sleep(1)
    resultado = s.recv(4096).decode()


    #---------------- NAO ALTERE A PARTIR DAQUI ----------------------------  
   
    fazLog(f'Conteudo na pasta remota: {resultado}')
    return resultado


def exercicio4(arquivo:str) -> bool:
    '''
    Verifica se o arquivo existe na máquina local

    Parametros:
    - arquivo: arquivo que será pesquisado

    Retorna: True se a arquivo existir, False caso contrário
    '''

    # DICAS: 
    # este comando é local, não envie par ao servidor remoto. 
    # Use o comando da biblioteca os, os.path.COMANDO(arquivo)
    # consulde a documentação no AVA ou pesquise no google para ver o comando correto

    if os.path.isfile(arquivo):
        print('O arquivo existe')  
        return True
    else:
        return False # atere conforme a definição da função


def exercicio5(s: socket, arquivo:str):
    '''
    Faz o upload de um arquivo texto para o servidor remoto

    Parametros:
    - s: socket tcp que representa a conexao o servidor remoto
    - arquivo: arquivo que será transmitido
    '''

    # DICA: complete os comandos indicados (eles estão no roteiro no AVA)
    # abrir o arquivo texto em modo leitura
    f = open(arquivo, "r")
    # ler uma linha do arquivo de cada vez
    # transmitir a linha para o servidor (converta a linha para bytes com enconde())
    for line in f:
        s.send(line.encode())
    # após transmitir a última linha fechar o arquivo
    f.close()



def exercicio6():
    '''
    Lista diretório corrente local e o seu conteudo
    '''

    # DICA: esses comandos são locais. São funções da biblioteca os

    dir = os.getcwd()
    conteudo = os.listdir()

    fazLog(f'Diretorio corrente: {dir}\n')
    fazLog(f'Conteudo: {conteudo}\n')


def exercicio7(dir: str):
    '''
    Cria a pasta dir no computador local e a define como novo diretório corrente
    
    Parametros:
    - dir: novo diretório corrente
    
    '''

    # DICA: esses comandos são locais. São funções da biblioteca os

    try:
        if not os.path.isdir(dir):
            os.makedirs(dir)
        os.chdir(dir)
    except Exception as e:
        fazLog(f'{e}\n')


def exercicio8(dir: str, file: str) -> str:   
    '''
    Cria um caminho a partir de um diretório e um arquivo de seguindo a sintaxe do sistema operacional

    Parameteros:
    - dir: diretório do arquivo
    - file: nome do arquivo

    Retorna:
    - O caminho para o arquivo na forma de uma string
    '''     

    return os.path.join(dir, file) 

def exercicio9(path: str) -> str:   
    '''
    Retorna o nome do arquivo a partir de um caminho (path)

    Parameteros:
    - path: caminho para o arquivo
    
    Retorna:
    - Nome do arquivo para o qual o caminho aponta
    '''     

    return os.path.basename(path)


def exercicio10(s: socket, file: str):  

    '''
    Salva os dados recebidos pelo socket em um arquivo local

    Parametros:
    - s: socket tcp que representa a conexao o servidor remoto
    - file: nome do arquivo local
    '''


    # DICA: complete os TODO que estão indicados no código abaixo
    # TODO: abra o arquivo em modo escrita binário

    f = open(file, "wb")
    while True:
    # Receber os dados da conexão em blocos de 1000 bytes
        try:
            data = s.recv(1000)
            if not data:
                break
            else:
                # TODO: escreva os dados recebidos no arquivo
                f.write(data)
                print(len(data))         
        except Exception as e:
            print(e)        
    # Quando o servidor encerrar a conexão, fechar o arquivo
    f.close()


#--------------------------------------------------------------------
# Incio do código principal

if __name__ == "__main__":    
    print('NAO EXECUTE O ARQUIVO exercicios.py. ELE É UMA BIBLIOTECA!!!')