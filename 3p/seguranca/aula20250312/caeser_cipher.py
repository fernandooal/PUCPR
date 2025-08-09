import random

def cripto(mensagem, chave):
    cripto = ""
    for c in mensagem:
        codigo = ord(c) + chave
        cripto += chr(codigo)
    return cripto

plain = 'Nada de novo no front'

tamanho = 14 #tamanho da chave em bits
espaco = 2 ** tamanho #valores que a chave pode assumir

chave = random.randint(1,espaco)
print(f'chave escolhida: {chave}')
cipher = cripto(plain, chave)
print(cipher)


#algoritmo simetrico -> mesmo algoritmo para criptografar e descriptografar
def brute_force(cipher, espaco):
    for chave in range(espaco):
        try:
            res = cripto(cipher, -chave)
            print(f'Chave = {chave} = {res}')
        except:
            print(f"a chave é menor que {chave}")
            break

# 1) Decodifique a mensagem Sfif%ij%st{t%st%kwtsy

# cipher = 'Sfif%ij%st{t%st%kwtsy'
# brute_force(cipher, espaco)


# 2) Qual o espaço de chaves do algoritmo? Qual o tamanho da chave?
# 3) Este algoritmo mantem padrão, como isso simplifica a quebra da criptografia?
# 4) É possível decifrar a mensagem sem testar todas as chaves?

def analise_frequencia(cipher):
    codigo = [ ord(c) for c in cipher ]
    freq = {}

    for c in codigo:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] = freq[c] + 1
            
    return sorted(freq.items(), key=lambda item: item[1])

res = analise_frequencia(cipher)
print(res)

print(res[-1][0] - ord('o'))
print(res[-2][0] - ord('o'))

print(res[-1][0] - ord(' '))
print(res[-2][0] - ord(' '))