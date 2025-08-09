contador = 0
soma = 0

while(contador < 10):
    numTemp = float(input("Digite um número: "))
    soma += numTemp
    contador += 1

print(f"A soma dos valores é {soma} e a sua média é de {soma/contador}")