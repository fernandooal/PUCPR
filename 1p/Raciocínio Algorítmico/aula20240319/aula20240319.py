nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (0-100): "))

media = (nota1 + nota2)/2

if(frequencia >= 75):
    if(media >= 7):
        print("Aprovado")
    elif(media >= 4):
        print("Recuperação")
    else:
        print("Reprovado por nota")
else:
    print("Reprovado por falta")
