#3. Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

nums = []

for i in range(3):
    nums.append(int(input("Digite um número inteiro: ")))

if(nums[0] > nums[1] + nums[2]):
    print("O primeiro número digitado é maior que a soma dos outros dois!")
else:
    print("O primeiro número digitado não é maior que a soma dos outros dois..")

    