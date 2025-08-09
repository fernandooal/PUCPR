import hmac
import hashlib
import os


def very_bad_hash(msg : str, size_bits = 32):
    hash_value = 0
    data = msg.encode()
    
    for b in data:        
        hash_value = (hash_value + b) % (2**size_bits) 

    return hash_value

def polinomial_hash(msg : str, size_bits = 32):

    hash_value = 0
    data = msg.encode()
    prime = 31  # A prime number often used in hashing algorithms

    for b in data:
        hash_value = (hash_value * prime + b) % (2**size_bits)   # Modulo to prevent overflow

    return hash_value

def calcula_hash_string(msg : str, alg = hashlib.md5 ):
    data = msg.encode()
    m = alg()
    m.update(data)
    return m.hexdigest()

def calcula_hash_file(file):

    alg = hashlib.sha256()

    if not os.path.isfile(file):
        print('O arquivo não existe')
        return None
    
    with open(file, 'rb') as f:
        data = f.read()
        alg.update(data)
    
    return alg.hexdigest()
    
def verifica_HASH(msg : str, hash : str, alg = hashlib.md5 ):

    if calcula_hash_string(msg, alg) == hash:
        print('Esta mensagem é verdadeira')
    else:
        print('Esta mensagem é falsa')


def calcula_HMAC(msg : str, segredo: str, alg=hashlib.md5):
    data = msg.encode()
    chave = segredo.encode()

    hmac_digest = hmac.new(chave, data, alg).digest()
    
    return hmac_digest.hex()

def verifica_HMAC(msg : str, segredo: str, hash :str, alg=hashlib.md5):
    if calcula_HMAC(msg, segredo, alg) == hash:
        print('Esta mensagem é verdadeira')
    else:
        print('Esta mensagem é falsa')

def meu_HMAC(key, message, alg=hashlib.md5):

    block_size = alg().block_size

    # If key length is greater than block size, hash it
    if len(key) > block_size:
        key = alg(key).digest()
    
    # If key length is less than block size, pad it
    if len(key) < block_size:
        key = key + b'\x00' * (block_size - len(key))
    
    o_key_pad = bytes((x ^ 0x5c) for x in key)
    i_key_pad = bytes((x ^ 0x36) for x in key)
    
    inner_hash = alg(i_key_pad + message).digest()
    outer_hash = alg(o_key_pad + inner_hash).hexdigest()

    return outer_hash




# Exercicio 1
# Verifique se consegue gerar colisão com o very_bad_hash
def exe1():
    msg1 = "Isto e um teste de HASH"
    msg2 = "Isso e um testf de HASH"
    
    print(very_bad_hash(msg1, 8))
    print(very_bad_hash(msg2, 8))
    
# Exercicio 2
# Verifique se polinomial_hash tem efeito avalanche

def exe2():
    msg1 = "Isso e um teste de HASH"
    msg2 = "Isso abcd teste de HASH122"
    
    print(polinomial_hash(msg1, 8))
    print(polinomial_hash(msg2, 8))

# Exercicio 3
# Verifique colisão e avalanche com o MD5 e SHA256
    
def exe3():
    msg1 = "Isto e um teste de HASH"
    msg2 = "Isso e um teste de HASH"
    
    print("====md5====")
    print(calcula_hash_string(msg1, hashlib.md5))
    print(calcula_hash_string(msg2, hashlib.md5))
    
    print("====sha256====")
    print(calcula_hash_string(msg1, hashlib.sha256))
    print(calcula_hash_string(msg2, hashlib.sha256))

# Exercicio 4
# Determine a diferença de tamanho do HASH do MD5 e SHA256
    
# Exercicio 5
# Complete a função que calcula o HASH de um arquivo e calcule o HASH de um PDF ou outro arquivo grande

print(calcula_hash_file("HashHMAC.py")) 


# Exercicio 6
# Charles é um MiTM. Ele interceptou uma mensagem de Alice para Bob. A mensagem tem um HASH em anexo. 
# Bob irá usar a função verifica_HASH. Ele pode ter certeza que a mensagem é integra e veio da Alice?
   
# Exercicio 7
# Teste a função calcula_HMAC com diferentes segredos. O valor HMAC depende apenas da mensagem?
   
# Exercicio 8
# Charles é um MiTM. Ele interceptou uma mensagem de Alice para Bob. A mensagem tem um HMAC em anexo. 
# Bob irá usar a função verifica_HMAC. Ele pode ter certeza que a mensagem é integra e veio da Alice?
        
# Exercicio 9
# Resolva o seguinte problema: como o HASH pode ser usado para proteger a senha durante a autenticação do usuário
# OBS. A solução precisa ser imune a ataques de repetição.
        
# Exercicio 10
# Resolva o seguinte problema: como o servidor pode salvar a senha do usuário em um banco de dados, sem expor a senha?











