'''
2) Implemente um programa em Python para ler do teclado
números. Caso o usuário forneça um numero igual a -1, o
programa deve fornecer a média dos números e encerrar
'''

soma = 0
contador = 0

numTemp = int(input("Digite um número para a soma (caso queira finalizar, digite -1): "))

while(numTemp != -1):
    contador += 1
    soma += numTemp
    numTemp = int(input("Digite um número para a soma (caso queira finalizar, digite -1): "))

if(contador != 0):
    print(f"O resultado da média dos números digitados é {(soma)/contador}")
else:
    print("Sem média - Não digitou valores o suficiente")