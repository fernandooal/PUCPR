
##### EX 1
# # representa o número decimal em binário (base 2 - digitos 0 até 1)
# print("Numero 192 (decimal => binario) = ", format(192,'8b')) 

# # representa o número decimal em hexadecimal (base 16 - digitos de 0 até 15)
# print("Numero 192 (decimal => hexa) = ",format(192, '1x'))

# # um digito em hexa corresponde a 4 bits
# print("Digito c (hexa => binario) = ", format(0xc, '4b')) 

# # um digito em hexa corresponde a 4 bits
# print("Digito f (hexa => binario) = ", format(0xf, '4b'))


##### EX 2

# # representa o número decimal 192 com um byte (palavra de 8 bits)
# print("Numero 192 (8 bits) = ", format(192,'b').zfill(8)) 
# print("De : ", 0b00000000, " até ", 0b11111111)
# print("De : ", 0x00, " até ", 0xff)

# # representa o número decimal 192 com um 2 bytes (palavra de 16 bits)
# print("Numero 192 (16 bits) = ", format(192,'b').zfill(16)) 
# print("De : ", 0b0000000000000000, " até ", 0b1111111111111111)
# print("De : ", 0x0000, " até ", 0xffff)

# # o maior número que pode ser representado é 2 elevado (TAMANHO DA PALAVRA - 1 )
# print("8 bits: ", 2**8)
# print("16 bits: ", 2**16, ' ou ', (2**8)*(2**8), ' ou ', (2 ** 8)**2)
# print("32 bits: ", 2**32, ' ou ', ' ou ', (2 ** 8)**4)
# print("64 bits: ", 2**64, ' ou ', ' ou ', (2 ** 8)**8)
# print("128 bits: ", 2**128, ' ou ', (2 ** 8)**16)

# # caso um computador teste 1000 chaves por segundo
# # quanto tempo levará para encontrar uma chave de 64 bits por força bruta?

# tamanho = 128
# taxa = 1000000000000

# espaco_chaves = (2**tamanho)

# tempo_s = espaco_chaves/taxa
# tempo_dias = tempo_s/(60*60*24)

# print(tempo_dias, 'dias')

# print(tempo_dias/365, 'anos')


##### EX 3 

# # 1) cria o arquivo como TEXTO
# f = open('teste.txt','w')
# tamanho = f.write('49192')
# print('Este arquivo tem ', tamanho, 'bytes')
# f.close()

# # 2) cria o arquivo como BINARIO
# f = open('testeb.txt','wb')
# print('Representação de 49192 em HEXA: ', format(49192,'1x'))
# tamanho = f.write(bytearray([0xc0, 0x28]))
# print('Este arquivo tem ', tamanho, 'bytes')
# f.close()

# # 3) abre o arquivo em modo TEXTO
# f = open('teste.txt','r')
# print('texto como texto: ', f.read())
# f.close()

# # 4) abre o arquivo em modo BINARIO
# f = open('testeb.txt','rb')
# res = f.read()
# print('binario como binario: ', res)
# print('o print anterior interpretou os bytes como caracteres')
# print('abaixo, os bytes estão sendo intepretado como hexa')
# for i in res:
#     print(format( i, 'x' ))
# f.close()

# # Exercicio 1: o que acontece se você abrir o arquivo testeb.txt com o notepad?
# # Exercicio 2: como interprentar o resultado do passo 4?
# # Exercicio 3: qual desses formatos é texto: PDF, DOC, HTML, JSON


##### EX 4

# codec = 'ansi'
# texto = 'mas é muita emoção'
# try:
#     embytes = texto.encode(codec)
#     print('em bytes:', embytes)
#     print('em string:', embytes.decode(codec))
# except Exception as e:
#     print(e, 'não consigo representar isso')  

# # OBS:
# # utf-16: adiciona um BOM FFFE no início do código
# # char: assume que o código convertido é UNICODE

# # Exercicio 1: teste os codecs ansi, utf-8 e utf-16?
# # Exercicio 2: verifique em que condições ascii não funciona.