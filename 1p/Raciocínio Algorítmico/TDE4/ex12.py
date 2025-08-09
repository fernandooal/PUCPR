#Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente, utilizando a seguinte
#estratégia de ordenação:
#• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
#• troque este elemento pelo primeiro;
#• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de menor valor com a segunda
#posição), depois os 18 elementos (trocando o de menor valor com a terceira posição), depois os 17, 16 e assim por diante,
#até restar um único elemento, o maior deles.
#Observação: este método de ordenação é conhecido como “Seleção Direta”

import random

nums = []

for i in range(20):
    nums.append(random.randint(0,100))

for i in range(20):
    min = nums[i]
    for j in range(i+1, len(nums)):
        if nums[j] < min:
            min = nums[j]
    indexMin = nums.index(min, i)
    nums[indexMin] = nums[i]
    nums[i] = min

print(nums)

'''
nums = []
sortedNums = []

for i in range(20):
    nums.append(random.randint(0,100))


while len(nums) > 0:
    min = nums[0]
    for num in nums:
        if num < min:
            min = num
    nums.remove(min)
    sortedNums.append(min)

print(sortedNums)
'''