peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (metros): "))

print(f"Seu IMC é e {round(peso/(altura**2),2)}")