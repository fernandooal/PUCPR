#!/usr/bin/env python3
from console import Console
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from datetime import datetime
import time

def fazLog(msg: str):
    '''
    Registra em um log a mensagem recebida
    - Não altere essa função
    - O arquivo log.txt deve sem entregue como resultado da tarefa
    - O log é único para cada equipe pois inclui portas aleatórias e horário de cada evento     
    '''
    print(msg, end='')
    f = open('log.txt', 'a')
    f.write(f'{datetime.now()} : {msg}')
    f.close()

def exercicio1(CONSOLE: list, SENSORES: dict):
    '''
    Lança o Console como uma Thread

    Parametros:
    CONSOLE: lista contendo usada para salvar o socket que representa a conexão TCP com o usuário
    SENSORES: dicionario que associa o id do sensor e sua conexão TCP
    '''

    # DICA: Para chamar uma thread: Thread(target=, args=) 
    # Use a chamada de TrataSensor em monitor.py como exemplo
    # Veja a definição da função Console e passe os argumentos na ordem correta
    # Não esqueça do start()
    
    t = Thread( target= Console, args=(CONSOLE, SENSORES,))
    t.start()

    # fazLog('esqueci de fazer o exercicio 1\n') # comente quando fizer o exercicio

def exercicio2(console: socket, dados: bytes):
    '''
    Se o usuário estiver conectado envie o dados RECEBIDOS pelos sensores para o Console
    - console precisa ser diferente de None
    
    Parametros:
    console: socket do tipo cliente que representa a conexão TCP com o usuário
    dados: dados recebidos pelo dispositivos de IoT
    '''
    # DICA: teste se o objeto de conexão is not None
    # Para enviar os dados execute: conexão.send( dados em bytes)
    # Observe o tipo dos argumentos da função para saber se precisa fazer conversão
    
    if console is not None:
        console.send(dados)
    
    # fazLog('esqueci de fazer o exercicio 2\n') # comente quando fizer o exercicio

def exercicio3(console: socket, SENSORES: dict):
    '''
    Envia para o usuario a lista de sensores conectados
    - console precisa ser diferente de None
    
    Parametros:
    console: socket do tipo cliente que representa a conexão TCP com o usuário
    '''

    # DICA: os IDs dos sensores conectados estão em SENSORES.keys()
    # Monte a mensagem da seguinte forma: msg = 'Sensores conectados: ' + ','.join(SENSORES.keys())
    # Para enviar a mensagem use console.send(bytes). 
    # Não esqueça de converter de string para bytes com encode()

    if console is not None:
        msg = 'Sensores conectados: ' + ','.join(SENSORES.keys())
        console.send(msg.encode())

    # fazLog('esqueci de fazer o exercicio 3\n') # comente quando fizer o exercicio

def exercicio4(SENSORES: dict, commando: str):
    '''
    Envia o mesmo comando para todos os sensores conectados
    
    Parametros:
    SENSORES: dicionario que associa o id do sensor e sua conexão TCP
    commando: string com o comando para o usuário - precisa ser convertida para bytes
    '''

    # DICA: a conexão de cada um dos sensores conectados está em SENSORES.values()
    # Faça um for para executar conexao_do_sensor.send(bytes)
    # Não esqueça de converter de string para bytes com encode()
    
    for conn in SENSORES.values():
        conn.send(commando.encode())
    
    # fazLog('esqueci de fazer o exercicio 4\n') # comente quando fizer o exercicio

def exercicio5(s: socket, addr: tuple):
    '''
    Faz a conexão com o monitor
    - caso o monitor responda retorna imediatamente
    - caso o monitor não responda, tenta novamente em intervalos de 10 segundos
    
    Parametros:
    s: socket do tipo cliente usado pelo dispositivo de IoT
    addr: tupla com o ip e porta do monitor
    '''
    
    # DICA: coloque o código abaixo em um while True
    # caso o não caia na exceção, coloque um return abaixo do connect
    # substitua o print da exceção por um time.sleep(10)

    while True:
        try:
            s.connect(addr)
            break
        except Exception as e:
            time.sleep(10)
        
    # fazLog('esqueci de fazer o exercicio 5\n') # comente quando fizer o exercicio

def exercicio6(s: socket, sensor: str, estado: str):
    '''
    Envia o estado de um sensor para o monitor 
    - formato da mensagem: sensor=estado\n
    
    Parametros:
    s: socket com a conexão entre o dispositivo de IoT e o monitor
    estado: string com o estado do dispositivo de IoT
    '''
    
    # DICA: monte a string a ser enviada f'{sensor}={estado}\n'
    # converta para bytes
    # envie com s.send(bytes)
    
    estado = f'{sensor}={estado}\n'
    s.send(estado.encode())

    # fazLog('esqueci de fazer o exercicio 6\n') # comente quando fizer o exercicio


    #---------------------------------------------------------------------
    # A ENTREGA DA SOMATIVA É ESTE ARQUIVO
    #EX SEGUINDO MONITOR, SENSORES E DEPOIS USUARIO
    # COPIE O RESULTADO DO ARQUIVO log.txt E COLE ABAIXO PARA ENTREGAR A TAREFA
    
    # 2024-09-24 21:16:56.711483 : MONITOR: aguardando dispositivos de IOT em 9999
    # 2024-09-24 21:16:56.711615 : CONSOLE: aguardando conexão do usuário em 8888
    # 2024-09-24 21:17:09.509059 : MONITOR: o sensor quarto registrou: ('127.0.0.1', 54326)
    # 2024-09-24 21:17:09.509097 : MONITOR: o sensor sala registrou: ('127.0.0.1', 54325)
    # 2024-09-24 21:17:09.510021 : MONITOR: o sensor cozinha registrou: ('127.0.0.1', 54327)
    # 2024-09-24 21:18:47.835666 : CONSOLE: O usuário conectou
    # 2024-09-24 21:18:47.842468 : CONSOLE RECEBEU: sala ligar
    # 2024-09-24 21:18:47.842699 : IOT sala: recebeu o comando=ligar
    # 2024-09-24 21:18:47.869761 : USUARIO RECEBEU: CONSOLE: digite SENSOR_ID COMANDO

    # 2024-09-24 21:18:48.847666 : CONSOLE RECEBEU: sala consulta
    # 2024-09-24 21:18:48.847923 : IOT sala: recebeu o comando=consulta
    # 2024-09-24 21:18:48.848170 : MONITOR: sensor sala enviou sala=ON
    # 2024-09-24 21:18:48.848517 : USUARIO RECEBEU: sala=ON

    # 2024-09-24 21:18:49.853184 : CONSOLE RECEBEU: todos consulta
    # 2024-09-24 21:18:49.853871 : IOT sala: recebeu o comando=consulta
    # 2024-09-24 21:18:49.853944 : IOT cozinha: recebeu o comando=consulta
    # 2024-09-24 21:18:49.854018 : IOT quarto: recebeu o comando=consulta
    # 2024-09-24 21:18:49.854131 : MONITOR: sensor sala enviou sala=ON
    # 2024-09-24 21:18:49.854285 : MONITOR: sensor quarto enviou quarto=OFF
    # 2024-09-24 21:18:49.854353 : MONITOR: sensor cozinha enviou cozinha=OFF
    # 2024-09-24 21:18:49.854557 : USUARIO RECEBEU: sala=ON

    # 2024-09-24 21:18:49.854705 : USUARIO RECEBEU: quarto=OFF
    # cozinha=OFF

    # 2024-09-24 21:18:50.858487 : CONSOLE RECEBEU: quarto shutdown
    # 2024-09-24 21:18:50.859202 : IOT quarto: recebeu o comando=shutdown
    # 2024-09-24 21:18:50.859574 : IOT quarto: SHUTDOWN, BYE!
    # 2024-09-24 21:18:50.859662 : MONITOR: sensor quarto encerrou
    # 2024-09-24 21:18:51.861716 : CONSOLE RECEBEU: quarto consulta
    # 2024-09-24 21:18:51.862295 : CONSOLE: O sensor quarto nao existe
    # 2024-09-24 21:18:51.862596 : USUARIO RECEBEU: O sensor quarto nao existe

    # 2024-09-24 21:18:51.862833 : USUARIO RECEBEU: Sensores conectados: sala,cozinha
    
    #EXERCICIO SEGUINDO SENSORES, MONITOR E USUARIO
    # 2024-10-01 17:59:55.646335 : MONITOR: aguardando dispositivos de IOT em 9999
    # 2024-10-01 17:59:55.646457 : CONSOLE: aguardando conexão do usuário em 8888
    # 2024-10-01 18:00:14.546578 : CONSOLE: O usuário conectou
    # 2024-10-01 18:00:14.554327 : CONSOLE RECEBEU: sala ligar
    # 2024-10-01 18:00:14.554453 : CONSOLE: O sensor sala nao existe
    # 2024-10-01 18:00:14.585699 : USUARIO RECEBEU: CONSOLE: digite SENSOR_ID COMANDO
    # O sensor sala nao existe
    # Sensores conectados: 
    # 2024-10-01 18:00:15.559629 : CONSOLE RECEBEU: sala consulta
    # 2024-10-01 18:00:15.559839 : CONSOLE: O sensor sala nao existe
    # 2024-10-01 18:00:15.560168 : USUARIO RECEBEU: O sensor sala nao existe

    # 2024-10-01 18:00:15.560339 : USUARIO RECEBEU: Sensores conectados: 
    # 2024-10-01 18:00:16.564992 : CONSOLE RECEBEU: todos consulta
    # 2024-10-01 18:00:17.570131 : CONSOLE RECEBEU: quarto shutdown
    # 2024-10-01 18:00:17.570783 : CONSOLE: O sensor quarto nao existe
    # 2024-10-01 18:00:17.571057 : USUARIO RECEBEU: O sensor quarto nao existe

    # 2024-10-01 18:00:17.571376 : USUARIO RECEBEU: Sensores conectados: 
    # 2024-10-01 18:00:18.575374 : CONSOLE RECEBEU: quarto consulta
    # 2024-10-01 18:00:18.575967 : CONSOLE: O sensor quarto nao existe
    # 2024-10-01 18:00:18.576324 : USUARIO RECEBEU: O sensor quarto nao existe

    # 2024-10-01 18:00:18.576637 : USUARIO RECEBEU: Sensores conectados: 