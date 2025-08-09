import random

def criarMatriz(linhas, colunas):
    matriz = []

    for i in range(linhas):
        vetor = []
        for j in range(colunas):
            vetor.append(0)
        matriz.append(vetor)
    
    return matriz

def criarCampoMinado(matriz, minas):
    for i in range(minas):
        linha = random.randint(0,len(matriz)-1)
        coluna = random.randint(0,len(matriz[0])-1)

        while matriz[linha][coluna] == 1:
            linha = random.randint(0,len(matriz)-1)
            coluna = random.randint(0,len(matriz[0])-1)
        
        matriz[linha][coluna] = 1

    return matriz


dificuldade = int(input("Digite a dificuldade que você quer jogar:\n0 - Iniciante;\n1 - Intermediário;\n2 - Avançado\n"))

while dificuldade < 0 or dificuldade > 2:
    dificuldade = int(input("Dificuldade inválida! Insira um valor entre 0 e 2: "))

if dificuldade == 0:
    campo = criarMatriz(9,9)
    minas = 10
elif dificuldade == 1:
    campo = criarMatriz(16,16)
    minas = 40
else:
    campo = criarMatriz(16,30)
    minas = 99

campoMinado = criarCampoMinado(campo, minas)

for linha in campoMinado:
    print(linha)