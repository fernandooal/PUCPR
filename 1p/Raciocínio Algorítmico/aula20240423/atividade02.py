palavra = input("Digite qualquer palavra: ").lower()
vogais = ['a', 'e', 'i', 'o', 'u']
vogalSoma = 0

i = 0
while i < len(palavra):
    if(palavra[i] in vogais):
        vogalSoma += 1
    i += 1

print(f"A palavra digitada possui {vogalSoma} vogais.")