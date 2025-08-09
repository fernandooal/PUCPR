#Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele gostaria de
#pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências
#foram detectadas.

nums = []

for i in range(10):
    nums.append(int(input("Digite um número inteiro: ")))

target = int(input("Digite o número que você gostaria de pesquisar: "))

indices = []

for i in range(len(nums)):
    if target == nums[i]:
        indices.append(i)

if len(indices) > 0:
    print(f"O número {target} foi encontrado {len(indices)} vez(es) no(s) índice(s) {indices}")
else:
    print("O número desejado não foi encontrado.")