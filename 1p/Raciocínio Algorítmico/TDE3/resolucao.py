#exercício 1
'''
i = 1

while(i < 100):
    print(i)
    i += 2
'''

#exercício 2
'''
i = 50

while(i >= 0):
    print(i)
    i -= 5
'''

#exercício 3
'''
i = -100

while(i <= 100):
    print(i)
    i += 10
'''

#exercício 4
'''
i = 1
multiplo = 0

while(multiplo < 96):
    multiplo = 4*i
    print(multiplo)

    i += 1
'''

#exercício 5
'''
n = int(input("Digite o número N: "))

i = 1

while(i <= n):
    if(i % 2 != 0):
        print(i)
    
    i += 1
'''

#exercício 6
'''
polegada = 1

while(polegada <= 20):
    print(f"{polegada} equivale à {polegada*2.54}cm")
    polegada += 1
'''

#exercício 7
'''
metros = 20000

while(metros <= 160000):
    print(f"{metros}m equivalem à {metros/1609.344} milhas")
    metros += 10000
'''

#exercício 8
'''
contador = 0
soma = 0

while(contador < 10):
    numTemp = float(input("Digite um número: "))
    soma += numTemp
    contador += 1

print(f"A soma dos valores é {soma} e a sua média é de {soma/contador}")
'''

#exercício 9
'''
li = int(input("Digite o limite inicial: "))
lf = int(input("Digite o limite final: "))

li += 1
while(li < lf):
    if(li % 3 == 0):
        print(li)
    li +=1
'''

#exercício 10
'''
moeda = input("Informe a moeda que você gostaria de cambiar (EUR, USD, GBP): ")
valor = float(input("Digite o valor que você gostaria de comprar dessa moeda: "))

if(moeda == "EUR"):
    valor = valor*5.46
elif(moeda == "USD"):
    valor = valor*5.07
elif(moeda == "GBP"):
    valor = valor*6.37
else:
    print("Moeda inválida.")

if(valor < 1000):
    print(f"Valor da operação: R${valor*1.05}")
else:
    print(f"Valor da operação: R${valor*1.03}")
'''

#exercício 11

i = 1
while(i <= 10):
    j = 1
    while(j <= 10):
        print(f"{i} * {j} = {i*j}")
        j += 1
    print("------------")
    i += 1