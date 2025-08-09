#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é
#triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.

num = int(input("Digite um número natural: "))

triangular = False

i = 1
while not triangular and i < num//4:
    if(i * (i+1) * (i+2) == num):
        print("Número triangular")
        triangular = True
    i += 1

if(not triangular):
   print("O número não é triangular")


