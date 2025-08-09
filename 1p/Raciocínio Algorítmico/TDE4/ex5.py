#5. Ler 4 números inteiros e calcular a soma dos que forem par. 

nums = []

soma = 0
for i in range(4):
    nums.append(int(input("Digite um número inteiro: ")))
    if(nums[i] % 2 == 0):
        soma += nums[i]

print(f"A soma dos números pares é {soma}")

                