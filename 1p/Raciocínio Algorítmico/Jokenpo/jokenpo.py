import random
import os

#criação de variáveis
player1 = "Máquina 1"
player2 = "Máquina 2"
winPlayer1 = 0
winPlayer2 = 0
continuePlaying = 1

#função para limpar o console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#função jogada da máquina
def randomPlay():
    x = random.randint(1,3)
    if(x == 1):
        return "pedra"
    elif(x == 2):
        return "papel"
    else:
        return "tesoura"

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
        play1 = input("Jogador 1, digite a sua jogada (pedra, papel ou tesoura): ").lower()
        while(play1 != "pedra" and play1 != "papel" and play1 != "tesoura"):
            play1 = input("Jogada inválida! Digite pedra, papel ou tesoura: ").lower()
        clear()
        play2 = input("Jogador 2, digite a sua jogada (pedra, papel ou tesoura): ").lower()
        while(play2 != "pedra" and play2 != "papel" and play2 != "tesoura"):
            play2 = input("Jogada inválida! Digite pedra, papel ou tesoura: ").lower()
        clear()
    elif(option == 2):
        #input jogador e jogada da máquina
        play1 = input("Jogador, digite a sua jogada (pedra, papel ou tesoura): ").lower()
        while(play1 != "pedra" and play1 != "papel" and play1 != "tesoura"):
           play1 = input("Jogada inválida! Digite pedra, papel ou tesoura: ").lower()
        play2 = randomPlay()
        clear()
    else:
        #jogada da máquina
        if(option == 3):
            play1 = randomPlay()
            play2 = randomPlay()
    
    #condicao de vitoria
    if(play1 == "papel" and play2 == "pedra" ) or (play1 == "tesoura" and play2 == "papel") or (play1 == "pedra" and play2 == "tesoura"):
        print(f"{player1} escolheu {play1}!\n{player2} escolheu {play2}...\nLogo, {player1} é o vencedor!\n")
        winPlayer1 += 1
    elif(play2 == "papel" and play1 == "pedra") or (play1 == "papel" and play2 == "tesoura") or (play1 == "tesoura" and play2 == "pedra"):
        print(f"{player1} escolheu {play1}...\n{player2} escolheu {play2}!\nLogo, {player2} é o vencedor!\n")
        winPlayer2 += 1
    else:
        print(f"{player1} e {player2} escolheram {play1}! Logo, deu empate!\n")
    
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