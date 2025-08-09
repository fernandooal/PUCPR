'''
3) Implemente um programa em Python para imprimir na tela o
somatório dos N primeiros números inteiros a partir do 1.
Sendo N lido do teclado
'''

num = int(input("Digite um número: "))

soma = 0
contador = 1
while contador <= num:
    soma += contador
    contador += 1

print(f"O resultado da soma é {soma}")