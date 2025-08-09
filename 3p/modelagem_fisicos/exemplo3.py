import time 

start = time.time()

#codigo nao otimizado

# numeros = list(range(1,10_000_000+1))

# soma = 0
# for numero in numeros:
#     soma += numero
# media = soma / len(numeros)

# print(f"O valor médio é: {media}")
# print(f"Levou: {time.time() - start} s")

# O valor médio é: 5000000.5
# Levou: 0.6402339935302734 s

#CODIGO OTIMIZADO
    
numeros = list(range(1,10_000_000+1))

primeiro = numeros[0]
ultimo = numeros[-1]

elementos = len(numeros)

resultado = (primeiro+ultimo) * (elementos/2) 

resultado = resultado/len(numeros)

print(f"A média através de lista é : {resultado}")
print(f"Levou: {time.time() - start} s")

# A média através de lista é : 5000000.5
# Levou: 0.09711694717407227 s