def calculadora(operacao, x, y):
    if operacao == "somar":
        return x+y
    elif operacao == "subtrair":
        return x-y
    elif operacao == "multiplicar":
        return x*y
    else:
        return x/y

operacao = input("Informe uma operação entre as seguintes:\nSomar;\nSubtrair;\nMultiplicar;\nDividir\n").lower()

while(operacao != "somar" and operacao != "subtrair" and operacao != "multiplicar" and operacao != "dividir"):
    operacao = input("Operação inválida! Digite somar, subtrair, multiplicar ou dividir: ").lower()

num1 = int(input("Digite o primeiro número para o cálculo: "))
num2 = int(input("Digite o segundo número para o cálculo: "))

print(f"O resultado da operação é {calculadora(operacao, num1, num2)}")