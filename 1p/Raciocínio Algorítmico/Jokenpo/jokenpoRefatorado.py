import random
import os

#criação de variáveis
player1 = "Máquina 1"
player2 = "Máquina 2"
winPlayer1 = 0
winPlayer2 = 0
continuePlaying = 1

#resultados
results =[[0,1,2], [2,0,1], [1,2,0]]

#função para limpar o console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#função jogada da máquina
def randomPlay():
    x = random.randint(0,2)

#função para imprimir o placar
def placar():
    print(f"Placar:\n{player1} -> {winPlayer1} vitórias\n{player2} -> {winPlayer2} vitórias\n")

    if(winPlayer1 > winPlayer2):
       print(f"Vencedor geral -> {player1}\n")
    elif(winPlayer2 > winPlayer1):
      print(f"Vencedor geral -> {player2}\n")
    else:
       print("Resultado geral -> Empate!\n")

clear()
print("Bem-vindo ao Jokenpo!\n")
print("0 - Sair;\n1 - Jogador x Jogador;\n2 - Jogador x Máquina;\n3 - Máquina x Máquina.\n")

option = int(input("Digite a modalidade de jogo que você gostaria: "))
while option < 0 or option > 3:
    option = int(input("Opção inválida! Digite um número entre 0 e 3: "))

#nome dos jogadores
if(option == 1):
    player1 = input("Digite o nome do jogador 1: ")
    player2 = input("Digite o nome do jogador 2: ")
elif(option == 2):
    player1 = input("Digite o nome do jogador 1: ")

clear()
#loop do jogo
while(continuePlaying == 1 and option != 0):
    if(option == 1):
        #input das jogadas (jogadores)
        play1 = int(input("Jogador 1, digite a sua jogada:\n0 - Pedra;\n1 - Papel\n2 - Tesoura.\n"))
        while(play1 < 0 or play1 > 2):
            play1 = int(input("Jogada inválida! Digite um número entre 0 e 2: "))
        clear()
        play2 = int(input("Jogador 2, digite a sua jogada:\n0 - Pedra;\n1 - Papel\n2 - Tesoura.\n"))
        while(play2 < 0 or play2 > 2):
            play2 = int(input("Jogada inválida! Digite um número entre 0 e 2: "))
        clear()
    elif(option == 2):
        #input jogador e jogada da máquina
        play1 = int(input("Jogador, digite a sua jogada:\n0 - Pedra;\n1 - Papel\n2 - Tesoura.\n"))
        while(play1 < 0 or play1 > 2):
           play1 = int(input("Jogada inválida! Digite um número entre 0 e 2: "))
        play2 = randomPlay()
        clear()
    else:
        #jogada da máquina
        if(option == 3):
            play1 = randomPlay()
            play2 = randomPlay()
    
    #condicao de vitoria
    if(results[play2][play1] == 0):
        print("Empate!")
    elif(results[play2][play1] == 1):
        print("O jogador 1 ganhou!")
        winPlayer1 += 1
    else:
        print("O jogador 2 ganhou!")
        winPlayer2 += 1
    
    print(f"Placar:\n{player1} -> {winPlayer1} vitórias\n{player2} -> {winPlayer2} vitórias\n")

    #continuar ou encerrar o jogo
    continuePlaying = int(input("Você gostaria de jogar novamente?\n0 - Não...\n1 - Sim!\n"))
    while(continuePlaying != 0 and continuePlaying != 1):
        continuePlaying = int(input("Opção inválida! Insira uma opção entre 0 (não) e 1 (sim): "))
    clear()

print(f"Placar:\n{player1} -> {winPlayer1} vitórias\n{player2} -> {winPlayer2} vitórias\n")

if(winPlayer1 > winPlayer2):
    print(f"Vencedor geral -> {player1}\n")
elif(winPlayer2 > winPlayer1):
  print(f"Vencedor geral -> {player2}\n")
else:
   print("Resultado geral -> Empate!\n")

print("Muito obrigado por jogar o meu Jokenpo!\n")
print("Feito por: Fernando Alonso =)")