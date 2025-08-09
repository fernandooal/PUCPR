import random

matriz = []

linhas = int(input("Digite um número de linhas: "))
colunas = int(input("Digite um número de colunas: "))

for i in range(linhas):
    vetor = []
    for j in range(colunas):
        vetor.append(random.randint(0,10))
    matriz.append(vetor)

for linha in matriz:
    print(linha)