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