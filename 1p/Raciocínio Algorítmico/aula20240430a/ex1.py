#Escreva um algoritmo que leia um vetor com 4 valores e apresente sua média

valores = []

i = 0
soma = 0
while i < 4:
    valores.append(float(input("Digite um valor: ")))

    soma += valores[i]
    i += 1

print(f"A média dos valores digitados é {soma/4}")
