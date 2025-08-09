li = int(input("Digite o limite inicial: "))
lf = int(input("Digite o limite final: "))

li += 1
while(li < lf):
    if(li % 3 == 0):
        print(li)
    li +=1