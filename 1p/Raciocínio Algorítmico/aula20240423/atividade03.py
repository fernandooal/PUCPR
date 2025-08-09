numeros = []

i = 0
while i < 10:
    numeros.append(int(input("Digite um número: ")))
    i += 1

continuar = 1
while continuar == 1:
    print(numeros)

    valorN = int(input("Digite um número para substituir algum outro no vetor: "))
    indice = int(input("Digite o índice do valor que gostaria de mudar: "))

    while(indice < 0 or indice > 9):
        indice = int(input("Valor de índice incorreto! Digite um valor entre 0 e 9: "))

    numeros[indice] = valorN
    print(f"O novo vetor é: {numeros}")

    continuar = int(input("Gostaria de fazer mais uma mudança?\n0 - Não;\n1 - Sim.\n"))
    while(continuar != 0 and continuar != 1):
        continuar = int(input("Valor inválido! Insira 0 para não ou 1 para sim: "))

print(f"Vetor final: {numeros}")
