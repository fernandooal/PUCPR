import datetime

anoNasc = int(input("Digite o ano que você nasceu: "))

anoAtual = datetime.datetime.now().year

print(f"A sua idade é {anoAtual - anoNasc}")