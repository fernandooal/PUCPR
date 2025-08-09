#Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido. Depois, crie dois outros
#vetores: vPares, contendo somente os números pares de vLido, e vImpares contendo somente os números ímpares de vLido.
#Os vetores vPares e vLido não deverão conter zeros. Mostre então os três vetores.

vLido = []
vPares = []
vImpares = []

for i in range(10):
    vLido.append(int(input("Digite um número inteiro: ")))
    while vLido[i] == 0:
        vLido[i] = int(input("O valor deve ser diferente de 0! Digite outro número: "))

    if(vLido[i] % 2 == 0):
        vPares.append(vLido[i])
    else:
        vImpares.append(vLido[i])

print(f"Valores lidos: {vLido}\nPares: {vPares}\nÍmpares: {vImpares}")
