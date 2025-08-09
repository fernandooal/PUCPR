import random

matriz = []

for i in range(3):
    vetor = []
    for j in range(3):
        vetor.append(random.randint(0,10))
    matriz.append(vetor)

for linhas in matriz:
    print(linhas)

soma = 0
for linhas in matriz:
    for valores in linhas:
        print(valores)
        soma += valores

print(f"A soma dos valores é {soma}")
