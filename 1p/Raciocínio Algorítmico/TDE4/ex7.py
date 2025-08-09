#A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor máximo e o valor mínimo
#de uma amostra. Elabore um programa que leia um vetor de 10 posições inteiras e então mostre o valor máximo, o valor
#mínimo e a amplitude amostral do conjunto fornecido.

nums = []
for i in range(10):
    nums.append(int(input("Digite um número inteiro: ")))

max = 0
min = nums[0]
for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]

    if nums[i] < min:
        min = nums[i]

print(f"Valor máximo: {max}\nValor Mínimo: {min}\nAmplitude amostral: {max-min}")