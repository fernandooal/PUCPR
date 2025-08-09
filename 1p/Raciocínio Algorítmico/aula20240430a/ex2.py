#Escreva um algoritmo que crie uma lista de tamanho 5 e imprima seus valores e em seguida a soma dos
#valores pares e ímpares
import random

valores = []

somaPar = 0
somaImpar = 0
i = 0
while i < 4:
    valores.append(random.randint(0,100))

    if valores[i] % 2 == 0:
        somaPar += valores[i]
    else:
        somaImpar += valores[i]
    
    i += 1

print(f"Vetor: {valores};\nSoma dos números pares: {somaPar};\nSoma números ímpares: {somaImpar}.")

