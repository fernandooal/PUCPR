matriz = [[10,20,30],
          [40,50,60],
          [70,80,90]]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])

for linha in matriz:
    for valor in linha:
        print(valor)