import random

def criarMatriz(linhas, colunas, x, y):
    matriz = []

    for i in range(linhas):
        vetor = []
        for j in range(colunas):
            vetor.append(random.randint(x,y))
        matriz.append(vetor)
    
    return matriz

def imprimirMatriz(matriz):
    for linha in matriz:
        print(linha)