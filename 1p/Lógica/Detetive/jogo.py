import random
import os

#função para limpar o console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_leaderboard(leaderboard):
    print("\nLeaderboard:\n")
    print("{:<15} {:<10}".format("Jogador", "Pontuação\n"))
    for line in leaderboard:
        print("{:<15} {:<10}".format(line[0], line[1]))

def show_intro():
    print("""
Jogo de detetive - Quem matou o Gomes?
    
Bem-vindo ao mundo da investigação, onde você será o juiz em um caso de assassinato que ocorreu durante um jantar na suntuosa mansão do senhor Gomes.
    
Gomes, um homem cuja presença era tão imponente quanto sua fortuna, era uma figura enigmática na sociedade. 
Ao longo dos anos, ele acumulou riquezas e influência, mas também colecionou uma série de inimigos ocultos nas sombras da alta sociedade. 
Seus segredos, tão bem guardados quanto os muros de sua mansão, eram motivo de especulação e temor entre aqueles que o conheciam.

Na esperança de resolver diferenças antigas e talvez até mesmo encontrar uma reconciliação, Gomes decidiu convidar seus maiores rivais para uma refeição em sua luxuosa residência. 
Entre os convites, estavam pessoas cujas vidas ele havia tocado de maneiras diversas: adversários comerciais, competidores políticos, e até mesmo aqueles que uma vez juraram vingança contra ele.

A atmosfera naquela noite estava carregada de expectativa e apreensão. 
Enquanto os convidados adentravam a mansão, podia-se sentir a tensão no ar, como se o próprio edifício estivesse ciente da iminente tragédia que se aproximava. 
Gomes, com sua típica expressão serena, recebia cada convidado com um sorriso cortês, mas seus olhos revelavam uma inquietação que não passava despercebida.

O jantar transcorria em meio a conversas educadas e sorrisos forçados, enquanto Gomes tentava manter o controle sobre a situação. 
No entanto, por trás das cortinas de cortesia, as antigas rivalidades ferviam, prontas para explodir a qualquer momento.

E então, como se o destino estivesse determinado a lançar sua sombra sobre aquela reunião, a tragédia se abateu sobre eles. 
Gomes, o anfitrião cuja influência era tão vasta quanto seu círculo de inimigos, caiu vítima de um ato de violência que chocou a todos os presentes.

A noite que deveria ter sido um momento de reconciliação e possível entendimento terminou em desastre, deixando para trás um mistério que desafiava até mesmo as mentes mais astutas. 

Você, como o juiz deste caso, tem a missão de descobrir quem foi o responsável por esse homicídio.
    
A cada rodada, você terá a oportunidade de coletar pistas ou até mesmo arriscar uma acusação, mas lembre-se: você só tem uma chance de acertar o verdadeiro assassino.
Cada pista que você utilizar terá um custo, então escolha sabiamente, pois sua pontuação final revelará sua eficácia como investigador.
A justiça de Gomes e a resolução deste mistério estão em suas mãos. Boa sorte!""")

def setup_game(names, descriptions):
    characters = {}
    for i in range(8):
        randomName = random.choice(names)  
        randomDesc = random.choice(descriptions)  
        characters[randomName] = randomDesc
        names.remove(randomName)  
        descriptions.remove(randomDesc)  
    deathCause = random.choice(["Envenenado", "Apunhalado", "Asfixiado"])
    return characters, deathCause

def print_characters(characters):
    print("\nSuspeitos:")
    randomNames = random.sample(list(characters.keys()), len(characters))
    for name in randomNames:
        print("- {} : {}".format(name, characters[name]))

def get_hints(deathCause, characters):
    if deathCause == "Envenenado":
        return [
            f"Se {list(characters.keys())[0]} não matou Gomes, então {list(characters.keys())[1]} estava na cozinha.",
            f"{list(characters.keys())[3]} ou {list(characters.keys())[1]} estavam na sala de estar no momento do assassinato.",
            f"{list(characters.keys())[5]} estava na sala de jantar se, e somente se, {list(characters.keys())[4]} matou Gomes com uma arma.",
            f"Se {list(characters.keys())[2]} estava na biblioteca, então {list(characters.keys())[3]} estava na cozinha",
            f"{list(characters.keys())[4]} estava no escritório ou {list(characters.keys())[5]} estava na sala de jantar.",
            f"{list(characters.keys())[6]} estava na varanda se, e somente se, {list(characters.keys())[4]} estava no escritório.",
            f"Se {list(characters.keys())[7]} estava na sala de jantar, então {list(characters.keys())[6]} estava na varanda.",
            f"{list(characters.keys())[7]} estava na sala de jantar e {list(characters.keys())[2]} estava na biblioteca.",
            f"Se {list(characters.keys())[4]} estava no escritório ou {list(characters.keys())[7]} estava na sala de jantar.",
            f"{list(characters.keys())[5]} estava na sala de jantar ou {list(characters.keys())[6]} estava na varanda."
        ]
    elif deathCause == "Apunhalado":
        return [
            f"Se {list(characters.keys())[0]} não matou Gomes, então {list(characters.keys())[1]} estava no banheiro.",
            f"{list(characters.keys())[3]} ou {list(characters.keys())[1]} estavam no quarto no momento do assassinato.",
            f"{list(characters.keys())[5]} estava na garagem se, e somente se, {list(characters.keys())[4]} matou Gomes com uma arma.",
            f"Se {list(characters.keys())[2]} estava no porão, então {list(characters.keys())[3]} estava no banheiro.",
            f"{list(characters.keys())[4]} estava no corredor ou {list(characters.keys())[5]} estava na garagem.",
            f"{list(characters.keys())[6]} estava no jardim se, e somente se, {list(characters.keys())[4]} estava no corredor.",
            f"Se {list(characters.keys())[7]} estava na garagem, então {list(characters.keys())[6]} estava no jardim.",
            f"{list(characters.keys())[7]} estava na garagem e {list(characters.keys())[2]} estava no porão.",
            f"Se {list(characters.keys())[4]} estava no corredor ou {list(characters.keys())[7]} estava na garagem.",
            f"{list(characters.keys())[5]} estava na garagem ou {list(characters.keys())[6]} estava no jardim."
            ]
    else:
        return [
            f"Se {list(characters.keys())[0]} não matou Gomes, então {list(characters.keys())[1]} estava na lavanderia.",
            f"{list(characters.keys())[3]} ou {list(characters.keys())[1]} estavam na sala de música no momento do assassinato.",
            f"{list(characters.keys())[5]} estava no terraço se, e somente se, {list(characters.keys())[4]} matou Gomes com uma arma.",
            f"Se {list(characters.keys())[2]} estava na adega, então {list(characters.keys())[3]} estava na lavanderia.",
            f"{list(characters.keys())[4]} estava na sala de jogos ou {list(characters.keys())[5]} estava no terraço.",
            f"{list(characters.keys())[6]} estava no escritório se, e somente se, {list(characters.keys())[4]} estava na sala de jogos.",
            f"Se {list(characters.keys())[7]} estava no terraço, então {list(characters.keys())[6]} estava no escritório.",
            f"{list(characters.keys())[7]} estava no terraço e {list(characters.keys())[2]} estava na adega.",
            f"Se {list(characters.keys())[4]} estava na sala de jogos ou {list(characters.keys())[7]} estava no terraço.",
            f"{list(characters.keys())[5]} estava no terraço ou {list(characters.keys())[6]} estava no pátio."
            ]

show_intro()

leaderboard = []

play = 1
while play == 1:
    names = ["Amanda", "Allan", "Marília", "Manoel", "Suzane", "Iran", "Bruno", "Carla"]
    descriptions = [
        "Socialite com um passado misterioso que mantém bem guardado.",
        "Empresário(a) com um histórico de trapaças e desonestidade.",
        "Escritor(a) conhecido(a) por sua inteligência e habilidade em criar enigmas.",
        "Chef com uma personalidade temperamental e uma habilidade notável para guardar segredos.",
        "Estudante de medicina promissor(a), cuja paixão por venenos é desconhecida.",
        "Biólogo(a) marinho com uma habilidade excepcional em manter seus verdadeiros pensamentos ocultos.",
        "Detetive particular com uma habilidade especial em ler pessoas.",
        "Advogado(a) com um histórico de defender pessoas culpadas."
    ]

    characters, deathCause = setup_game(names, descriptions)
    print_characters(characters)
    print(f"\nGomes morreu {deathCause.lower()}!\n")

    dicas = get_hints(deathCause, characters)
    chances = 10

    while chances > 0:
        choice = int(input(f"Escolha uma opção:\n0 - Dica ({chances} restantes)\n1 - Adivinhar\n"))
        if choice == 1:
            tentativa = input("Digite o nome do assassino: ")
            if tentativa.lower() == list(characters.keys())[0].lower():
                print("Parabéns! Você encontrou o assassino.")
                break
            else:
                print("Infelizmente você errou. O assassino era:", list(characters.keys())[0])
                chances = 0
        elif choice == 0:
            if dicas:
                tempDica = random.randint(0, len(dicas)-1)
                print(f"Dica: {dicas[tempDica]}")
                dicas.pop(tempDica)
            chances -= 1
        else:
            print("Opção inválida. Tente novamente.")

    if chances == 0 and choice != 1:
        tentativa = input("Você usou todas as dicas! Agora deve adivinhar: Quem é o assassino? ")
        if tentativa.lower() == list(characters.keys())[0].lower():
            print("Parabéns! Você encontrou o assassino.")
        else:
            print("Infelizmente você errou. O assassino era:", list(characters.keys())[0])

    print(f"Você conseguiu finalizar essa partida com uma pontuação de {chances} pontos!")
    playerName = input("Digite seu nome para adicionar sua pontuação no placar geral: ")
    leaderboard.append([playerName, chances*10])

    play = int(input("\nGostaria de iniciar outro jogo?\n0 - Não\n1 - Sim\n"))
    while play != 0 and play != 1:
        play = int(input("Opção Inválida! Informe 0 para não ou 1 para sim: "))
    
    clear()

show_leaderboard(leaderboard)

print("\nObrigado por jogar =)")