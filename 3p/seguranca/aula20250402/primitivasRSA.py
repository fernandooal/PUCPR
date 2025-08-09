import random
import math

# Testa se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Gera um número primo randômico
def generate_prime(bit_length):
    while True:
        prime_candidate = random.getrandbits(bit_length)
        if is_prime(prime_candidate):
            return prime_candidate

# Encontra o maior divisor comum a dois números (um número é co-primo quando GCD é 1)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Calcula d (modular multiplicative inverse)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Gera as chaves RSA
def generate_rsa_keys(bit_length):
    # Escolhe dois números primos
    p = generate_prime(bit_length // 2)
    q = generate_prime(bit_length // 2)
    
    # Calcula n
    n = p * q

    print(f'PASSO1: escolhe dois números primos p={p} e q={q}' )
    print(f'PASSO2: calcula n=p*q, n={n}')
    print('OBS: O valor de n é o valor máximo que pode ser criptografado')

    # Calcula o phi (Euler's totient function)
    phi = (p - 1) * (q - 1)
    print(f'PASSO 3: calcula phi = (p-1)*(q-1), phi={phi}')
    
    # Escolhe um inteiro entre 1 < e < phi e gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    print(f'PASSO 4: escolhe um número inteiro (e), tal que 1 < e < phi e (e) é co-primo com (n), e={e}')

    # Calcula d 
    d = mod_inverse(e, phi)
    print(f'PASSO 5: calcula d de tal forma que e*d % (p-1)(q-1) = 1, d={d}')
    print(f'VERIFICACAO: e*d % (p-1)(q-1) = {e*d % ((p-1)*(q-1))}')
    
    # Public key: (n, e), Private key: (n, d)
    print(f'PASSO 6: Determina a chave Pública (n,e) = {n,e} e Privada (n,d) = {n,d}')
    return ((n, e), (n, d))

# Function to encrypt a message
def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message


print('\nGERACAO DAS CHAVES:')
bit_length = 32  # Ajustar o valor conforme desejado
public_key, private_key = generate_rsa_keys(bit_length)

print('\nCRIPTOGRAFIA s = m**e % n')
message = "Estou criptografando um caractere de cada vez, mas poderia ser mais!"
print("Plain Text:", message)

encrypted_message = encrypt(message, public_key)
print("Cipher Text:", encrypted_message)

print('\nDESCRIPTOGRAFIA m = s**d % n')
decrypted_message = decrypt(encrypted_message, private_key)
print("Mensagem recuperada:", decrypted_message)
