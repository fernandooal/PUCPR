import time

start = time.time()

#codigo nao otimizado

# numeros = list(range(1,10_000_000+1))

# a = 0

# for numero in numeros:
#     a += numero
    
# print(f"A soma através de lista é : {a}")
# print(f"Levou: {time.time() - start} s")

# A soma através de lista é : 50000005000000
# Levou: 0.6344020366668701 s


# CODIGO OTIMIZADO - SOMA DE GAUSS/SOMA DE PA
numeros = list(range(1,10_000_000+1))

primeiro = numeros[0]
ultimo = numeros[-1]

elementos = len(numeros)

resultado = (primeiro+ultimo) * (elementos/2) 

print(f"A soma através de lista é : {resultado}")
print(f"Levou: {time.time() - start} s")
# A soma através de lista é : 50000005000000.0
# Levou: 0.10549783706665039 s