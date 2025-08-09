#2. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.

j = 1
k = 0
for i in range(110):
    print(f"{j} * {k} = {(j) * k}")
    k += 1
    if(k > 10):
        j += 1
        k = 0
        print("------------------")
    
