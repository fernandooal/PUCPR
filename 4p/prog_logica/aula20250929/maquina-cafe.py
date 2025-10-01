soma = 0

while True:
    try:    
        valor = int(input('Digite o valor inserido: '))
        
        if (valor != 5 and valor != 10 and valor != 25 and valor != 50):
            raise Exception
        
        soma += valor
        
        if(soma >= 35):
            print('venda!')
            soma -= 35
    except:
        print('Moeda inválida...')


