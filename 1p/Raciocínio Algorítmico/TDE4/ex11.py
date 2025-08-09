#Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra um conjunto de 6
#números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do usuário (sem repetição) e indique quantos
#acertos ele teve.

import random

numerosJogador = []
numerosMega = []
erroRep = False
erroInt = False

while len(numerosJogador) < 6:
    if(erroRep):
        numeroTemp = int(input("Número repetido! Insira um valor diferente: "))
        erroRep = False
    elif(erroInt):
        numeroTemp = int(input("Valor inválido! Digite um número entre 1 e 60: "))
        erroInt = False
    else:
        numeroTemp = int(input("Digite um número: "))

    if(numeroTemp > 0 and numeroTemp < 60):
        if(numeroTemp not in numerosJogador):
            numerosJogador.append(numeroTemp)
        else:
            erroRep = True
    else:
        erroInt = True
    
while len(numerosMega) < 6:
    numeroTemp = random.randint(1,60)
    if(numeroTemp > 0 and numeroTemp < 60):
        if(numeroTemp not in numerosMega):
            numerosMega.append(numeroTemp)


print(f"Números jogados: {numerosJogador};\nNúmeros sorteados: {numerosMega}")

acertos = 0
i = 0
while i < 6:
    if numerosJogador[i] in numerosMega:
        acertos += 1
    i += 1

print(f"Total de acertos: {acertos}")
