import comparaRC4AES as AES
import os
from base64 import b64encode

'''
EXERCICIO: 

Faça as chamadas para criptografar e descriptografar com AES em cada um dos 4 modos: ECB, CBC, CTR e GCM 
O modo ECB foi fornecido como exemplo. Inclua o teste para os outros 3 modos CBC, CTR e GCM 
plaintext = 'TESTE DA EQUIPE X' ou 'TESTE DO ESTUDANTE XX' 

PARA ENTREGAR A ATIVIDADE COPIE O RESULTADO DO PRINT NO FINAL DO ARQUIVO

'''
    
msg = 'TESTE DO ESTUDANTE FERNANDO ALONSO'    
plaintext = msg.encode('UTF-8')

if len(plaintext) % 16 != 0:
    plaintext = plaintext + bytearray(16 - len(msg)%16)
    
chave = os.urandom(16)


# Copie e modifique esta seção para os 3 modos restantes
#-----------------------------------------------------
modo = 'ECB'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    plaintext = AES.decifra_AES(ciphertext, chave, modo)
    print('Plaintext:', plaintext.decode())

except Exception as e:    
    print(e)
#-----------------------------------------------------

modo = 'CBC'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    plaintext = AES.decifra_AES(ciphertext, chave, modo, iv)
    print('Plaintext:', plaintext.decode())

except Exception as e:    
    print(e)
#-----------------------------------------------------

modo = 'CTR'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    plaintext = AES.decifra_AES(ciphertext, chave, modo, iv)
    print('Plaintext:', plaintext.decode())

except Exception as e:    
    print(e)
#-----------------------------------------------------

modo = 'GCM'
print(f'\nTESTE DO MODO {modo}')
print( 'chave:', [ b for b in chave ] )
try:
    ciphertext, iv, tag = AES.cifra_AES(plaintext, chave, modo)

    if iv is not None: print( 'iv:', [ b for b in iv ] )
    if tag is not None: print( 'tag:', [ b for b in tag ] )
    print('Ciphertext (B64):', b64encode(ciphertext))

    plaintext = AES.decifra_AES(ciphertext, chave, modo, iv, tag)
    print('Plaintext:', plaintext.decode())

except Exception as e:    
    print(e)
#-----------------------------------------------------

'''
--------------------------------------------------------------------------------------------------------
COLOQUE O PRINT COM OS RESULTADOS AQUI

TESTE DO MODO ECB
chave: [232, 189, 45, 113, 3, 226, 214, 28, 86, 114, 254, 114, 211, 122, 114, 35]
O modo ECB critografa cada bloco separadamente
Ciphertext (B64): b'mbeUhmfEXneaDCTj7mLSzaWyoiIz5GuGG8XtL/V8rUt+fCdVNE8TAS0BSisPyxs1'
Plaintext: TESTE DO ESTUDANTE FERNANDO ALONSO

TESTE DO MODO CBC
chave: [232, 189, 45, 113, 3, 226, 214, 28, 86, 114, 254, 114, 211, 122, 114, 35]
O modo CBC faz um XOR de cada bloco com o anterior e cria um problema de paralelismo
iv: [77, 200, 118, 11, 105, 190, 249, 212, 159, 185, 208, 251, 211, 23, 211, 36]
Ciphertext (B64): b'TLNWhtQsNFsdn05TSxnFIY1VyJLSpTWec89B93vpDeu0Xp0pnqQJvl8miWeZ/RFT'
Plaintext: TESTE DO ESTUDANTE FERNANDO ALONSO

TESTE DO MODO CTR
chave: [232, 189, 45, 113, 3, 226, 214, 28, 86, 114, 254, 114, 211, 122, 114, 35]
O modo CTR usa o AES para gerar um keystream para um XOR cipher
iv: [110, 31, 40, 19, 183, 252, 190, 49, 185, 69, 171, 124, 218, 111, 65, 32]
Ciphertext (B64): b'XpRxVnDpKkC97CjLTVoRfaNaUshZdwasY3+Q/ydjggaX7OmFxZ6ZQDB0Dbl1JLIf'
Plaintext: TESTE DO ESTUDANTE FERNANDO ALONSO

TESTE DO MODO GCM
chave: [232, 189, 45, 113, 3, 226, 214, 28, 86, 114, 254, 114, 211, 122, 114, 35]
O modo GCM é similar ao CTC mais adiciona um tag de autenticacao
iv: [215, 194, 245, 44, 116, 53, 166, 201, 215, 76, 145, 252, 84, 106, 1, 65]
tag: [9, 62, 88, 73, 169, 30, 13, 36, 58, 123, 66, 10, 4, 184, 219, 199]
Ciphertext (B64): b'HgmRh5+TKFecphu/URSOmuyE5T5WBL3i4LW7OBpJFQmapOlnG06worrSPSD2Cfq3'
Plaintext: TESTE DO ESTUDANTE FERNANDO ALONSO

obs: professor, acredito que no teste do modo GCM aquele texto pronto está errado, ele diz que o GCM é similar ao CTC, creio que deveria ser CTR.
'''