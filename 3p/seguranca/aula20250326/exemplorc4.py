from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def ksa(key):
    """
    Key-Scheduling Algorithm (KSA) for RC4.
    """
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, length):
    """
    Pseudo-Random Generation Algorithm (PRGA) for RC4.
    """
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        keystream.append(keystream_byte)
    return bytes(keystream)

while True:
    chave = input('Digite a chave secreta: ')
    
    chave = chave.encode() # chave em bytes
    
    meu_cipher = Cipher( algorithms.ARC4(chave), mode=None)
    cifrador = meu_cipher.encryptor()
    decifrador = meu_cipher.decryptor()
    
    mensagem = input('Digite a mensagem: ').encode()
    
    ciphertext = cifrador.update(mensagem)
    print('Mensagem cifrada: ', ciphertext.hex())
    plaintext = decifrador.update(ciphertext)
    print('Mensagem decifrada: ', plaintext.decode())
