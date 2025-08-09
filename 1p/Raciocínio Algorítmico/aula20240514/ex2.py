import random

matriz = []

for i in range(4):
    vetor = []
    for j in range(4):
        vetor.append(random.randint(0,10))
    matriz.append(vetor)

for linhas in matriz:
    print(linhas)

j = 0
for i in range(4):
    print(matriz[i][j])
    j += 1