#Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores positivos. Modifique
#então o vetor de forma que, tenhamos primeiro todos os números pares, depois, os números impares. Mostre o vetor antes de
#depois da modificação.

nums = []
sortedNums = []

for i in range(10):
    nums.append(int(input("Digite um número natural: ")))
    while nums[i] < 0:
        nums[i] = int(input("Valor negativo! Insira um número positivo: "))
    
    if nums[i] % 2 == 0:
        sortedNums.append(nums[i])

for i in range(len(nums)):
    if nums[i] % 2 == 1:
        sortedNums.append(nums[i])

print(f"Vetor original: {nums}\nVetor modificado: {sortedNums}")


    
