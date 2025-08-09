#Desenvolva um programa para o “Jogo da Forca”. Para tal, crie um vetor de strings inicializado com um conjunto
#de palavras-chave (por exemplo: nomes de capitais do Brasil, ou times de futebol ou Países da América do Sul
#etc). Sorteie uma das palavras para ser o segredo e forneça seis vidas para o usuário acertar o segredo.A cada
#rodada informe o número de vidas disponíveis e a disposição das letras acertadas e ausentes na palavra
#segredo (lembre de quando brincava com este jogo em caderno na infância), mostre também quais as letras que já
#foram usadas (e não compute acerto ou erro no caso do usuário repetir uma letra já fornecida)
import random

palavrasChave = ["brasil", "colombia", "peru", "equador", "argentina", "paraguai", "guiana-francesa", "venezuela", "chile", "uruguai", "suriname", "guiana", "bolivia"]

print("Bem-vindo ao jogo de Forca!\n")

#escolhendo uma palavra-chave aleatória
palavraJogo = palavrasChave[random.randint(0,len(palavrasChave)-1)]

#criando um vetor para imprimir o progresso do jogador
tentativaJogador = ['_']*len(palavraJogo)

tentativas = []
vidas = 6
acertos = 0
letraRepetida = False
letraInvalida = False
while vidas > 0 and acertos < len(palavraJogo):
    print(f"Vidas disponíveis: {vidas}\n")

    #ajustando palavras compostas
    if "-" in palavraJogo:
        indice = palavraJogo.index('-')
        tentativaJogador[indice] = '-'

        acertos += 1
        print(tentativaJogador)
    else:
        print(tentativaJogador)

    if letraRepetida:
        letraTemp = input("Letra já jogada! Tente outra: ")
    elif letraInvalida:
        letraTemp = input("Jogada inválida! Digite apenas uma letra: ")
    else:
        letraTemp = input("Digite uma letra: ")
    
    #verificação de entradas inválidas
    if letraTemp in tentativas:
        letraRepetida = True
    else:
        letraRepetida = False

    if len(letraTemp) > 1:
        letraInvalida = True
    else:
        letraInvalida = False

    tentativas.append(letraTemp)

    #alterando letra na tentativa em caso de acerto
    if(letraTemp in palavraJogo) and letraRepetida == False and letraInvalida == False:
        indices = [i for i, x in enumerate(palavraJogo) if x == letraTemp]
        
        for i in range (len(indices)):
            indiceTemp = indices[i]
            tentativaJogador[indiceTemp] = letraTemp
        print(f"\nAcertou!\n")
        acertos += i
    #letra errada
    else:
        print(f"\nErrou..\n")
        vidas -= 1

    tentativas.sort()
    print(f"Letras jogadas: {tentativas}\n")

if(vidas > 0):
    print("Você ganhou!\n")
else:
    print("Você perdeu =(")

palavraFinal = ''.join(palavraJogo)
print(f"A palavra-chave era: {palavraFinal}")