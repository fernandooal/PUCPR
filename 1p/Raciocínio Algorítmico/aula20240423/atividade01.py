inteiros = []

i = 0
while i < 10:
    inteiros.append(int(input("Digite um número inteiro: ")))
    i += 1

j = 0
while j < 10:
    print(f"Posição {j}: {inteiros[j]}")
    j += 1