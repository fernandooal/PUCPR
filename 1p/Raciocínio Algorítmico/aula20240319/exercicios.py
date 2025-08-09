# Exercício 1

'''
peso = float(input("Digite o peso do boxeador: "))

if(peso >= 88):
    print("Categoria: Super Pesado")
elif(peso >= 76):
    print("Categoria: Pesado")
elif(peso >= 60):
    print("Categoria: Leve")
elif(peso >= 50):
    print("Categoria: Pluma")
else:
    print("Categoria: Palha")
'''

# Exercício 2

'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if(num1 < num2):
    if(num1 < num3) and (num2 < num3):
        print(num1, num2, num3)
    elif(num1 > num3):
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
elif(num2 < num3):
    if(num1 < num3):
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    print(num3, num2, num1)
'''

# Exercício 3

'''
nota = float(input("Digite a sua nota (0-10): "))
frequencia = float(input("Digite a sua frequência (0-100): "))

if(frequencia > 70):
    if(nota > 9):
        print('A')
    elif(nota > 8):
        print('B')
    elif(nota > 7):
        print('C')
    elif(nota > 6):
        print('D')
    elif(nota > 4):
        print('E')
    else:
        print('F')
else:
    print("Reprovado por falta")
'''

# Exercício 4

'''
horas = int(input("Digite a parte inteira da hora atual: "))
minutos = int(input("Digite os minutos da hora atual: "))

if(horas >= 7 and horas <= 23):
    if(horas == 23) and (minutos > 10):
        print("Fora do horário de funcionamento.")
    elif(horas == 7) and (minutos < 30):
        print("Fora do horário de funcionamento.")
    else:
        print("Dentro do horário de funcionamento.")
else:
    print("Fora do horário de funcionamento.")
'''
