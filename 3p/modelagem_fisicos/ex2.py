import time
import random
import math

tempo_lista_start = time.time()

lista = [random.randint(1,1_000_000) for _ in range(100_000)]

tempo_lista_end = time.time()

tempo_lista = tempo_lista_end - tempo_lista_start

tempo_sort_start = time.time()

lista.sort()

tempo_sort_end = time.time()

tempo_sort = tempo_sort_end - tempo_sort_start

tempo_primos_start = time.time()

primos = []
for number in lista:
    if(number == 1 or number == 2):
        primos.append(number)
    elif(number % 2 == 0):
        continue
    else:
        ehprimo = True
        for i in range(3, int(math.sqrt(number)) + 1):
            if number % i == 0:
                ehprimo = False
                break
        if ehprimo == True:
            primos.append(number)
            
tempo_primos_end = time.time()

tempo_primos = tempo_primos_end - tempo_primos_start

tempo_print_primos_start = time.time()

print(primos)

tempo_print_primos_end = time.time()

tempo_print_primos = tempo_print_primos_end - tempo_print_primos_start

tempo_total = time.time() - tempo_lista_start

print("Tempo lista: " , tempo_lista)
print("Tempo sort: " , tempo_sort)
print("Tempo primos: " , tempo_primos)
print("Tempo primos print: " , tempo_print_primos)
print("\nTempo total: " , tempo_total)