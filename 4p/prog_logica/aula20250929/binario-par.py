# binario = input('Digite o binário: ')

# count = 0
# for i in range(0, len(binario)):
#     if int(binario[i]) == 1:
#         count += 1

# if count % 2 == 0:
#     print('par')
# else:
#     print('impar')
 
#sem aritmetica   
#0
def s1(bin):
    if len(bin) == 0:
        print('par')
        return
        
    if bin[0] == '1':
        s2(bin[1:])
    else:
        s1(bin[1:])

#1
def s2(bin):
    if len(bin) == 0:
        print('impar')
        return
        
    if bin[0] == '1':
        s1(bin[1:])
    else:
        s2(bin[1:])
        
binario = input('Digite o binário: ')
s1(binario)