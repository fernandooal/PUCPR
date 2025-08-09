#Solicite 5 números para o usuário, armazene em um vetor e mostre a soma dos números pares.
numeros = [0]*5
soma = 0

i = 0
while(i < len(numeros)):
    numeros[i] = int(input("Digite um número: "))

    if(numeros[i] % 2 == 0):
        soma += numeros[i]
    
    i += 1

print(soma)