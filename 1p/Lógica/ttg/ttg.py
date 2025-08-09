tabelaVerdade = [['p', 'q'], ['V', 'V'], ['V', 'F'], ['F', 'V'], ['F', 'F']]

def negacaoValoresTabela():
    tabelaVerdade[0].extend(['~p', '~q'])
    
    for linha in tabelaVerdade[1:]:
        negacao_p = 'F' if linha[0] == 'V' else 'V'
        negacao_q = 'F' if linha[1] == 'V' else 'V'
        linha.extend([negacao_p, negacao_q])
    
    for linha in tabelaVerdade:
        print(linha)

negacaoValoresTabela()
