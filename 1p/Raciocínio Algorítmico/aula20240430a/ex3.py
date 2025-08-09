#Ordene um vetor de 100 números inteiros gerados aleatoriamente.
import random

valores = []

i = 0
while i < 100:
    valores.append(random.randint(0,100))

    i += 1

valores.sort()

print(valores)