from base64 import b64encode, b64decode

def xor_cipher(plain, key):
    cripto = ""
    for c in plain:
        codigo = ord(c) ^ key
        cripto += chr(codigo)
    return cripto

def xor_cipher_b64(plain, key):
    c_bytes = [ ord(c) ^ key for c in plain ]
    return b64encode(bytearray(c_bytes))

def xor_decipher_b64(cipher_b64, key):
    c_bytes = b64decode(cipher_b64)
    plain = [ chr(c ^ key) for c in c_bytes ]
    return plain

chave = 253 % 256 # (% é usado para fazer truncamento)
print(chave)

plain = 'isto é um teste muito estranho'
cipher = xor_cipher_b64(plain, chave)

print('CRIPTO:', cipher)
print('DECRIPTO:', xor_decipher_b64(cipher, chave) )

# EXERCICIO 1: Copie o cipher do prompt do VSCcode e coloque na variável cipher2
# Veja se a descriptografia funciona

cipher2 = b'lI6Jkt0U3YiQ3YmYjomY3ZCIlImS3ZiOiY+ck5WS'
print('DECRIPTO 2:', ''.join(xor_decipher_b64(cipher2, chave)))

# EXERCICIO 2: Substitua as chamadas pelas versões b64 e repita o teste com o
# copiar e colar anterior
