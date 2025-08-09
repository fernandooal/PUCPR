'''
4) Escreva um programa que recebe 10 números do teclado e
exibe a quantidade de números pares e impares lidos
'''

i = 0

par = 0
impar = 0
while i < 10:
    numTemp = int(input("Digite um número inteiro: "))

    if(numTemp % 2 == 0):
        par += 1
    else:
        impar += 1

    i += 1

print(f"Você digitou {par} números pares e {impar} números ímpares.")