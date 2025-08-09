import os

#função para limpar o console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#display estoque
def displayStock(products):
    print("\nVending Machine:\n")
    print(f"{'ID':<5} {'Produto':<20} {'Preço':<10} {'Estoque':<10}")
    print("-" * 45)
    for product in products:
        print(f"{product[0]:<5} {product[1]:<20} {(product[2]/100):<10} {product[3]:<10}")

#display das opções do usuário
def optionProducts(products):
    displayStock(products)
    print("\nOpções especiais:\n")
    print("-1 - Modo administrador")
    print(" 0 - Desligar máquina\n")

#função para garantir escolha válida do usuário
def checkProduct(products, available, inStock):
    #output de acordo com a escolha do usuário
    if not available:
        print(f"Produto indisponível, digite outro ID dentre as opções: ")
    elif not inStock:
        print(f"Produto sem estoque disponível, favor escolher outro dentre as opções: ")
    else:
        print("Escolha um dos produtos a seguir pelo seu ID: ")
    
    optionProducts(products)
    
    #verificando se o input é válido
    while True:
        try:
            product = int(input(""))
            break
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
    
    #análise lógica do input 
    if product == 0:
        return 0
    elif product == -1:
        return -1
    elif product < 1 or product > len(products):
        clear()
        return checkProduct(products, False, True)
    elif products[product-1][3] <= 0:
        clear()
        return checkProduct(products, True, False)
    else:
        return product

#cálculo do troco
def calculateChange(change, changeModel, changeAvailable):
    #criando um backup temporário do troco disponível
    tempChangeAvailable = changeAvailable
    #array para mostrar o troco
    displayChange = []
    for i in range(len(changeModel)):
        enoughChange = True
        #verificando se a nota/moeda consegue dividir o troco
        quantityMoney = change // changeModel[i]
        #se tiver nota/moeda para o troco mas não o suficiente para completar
        if quantityMoney > changeAvailable[i]:
            quantityMoney = changeAvailable[i]
            #caso para a moeda de 1 centavo não entrar no troco a menos q seja suficiente
            if i == 12:
                enoughChange = False
        
        #condição para adicionar a nota/moeda no troco    
        if quantityMoney > 0 and enoughChange:
            if changeModel[i] > 100:
                displayChange.append(f"{quantityMoney} nota(s) de R${changeModel[i] / 100:.2f}")
            else:
                displayChange.append(f"{quantityMoney} moeda(s) de R${changeModel[i] / 100:.2f}")
            #subtrair dos arrays e do troco os valores utilizados
            change -= quantityMoney * changeModel[i]
            changeAvailable[i] -= quantityMoney

    #output de acordo com a situação do troco
    if change > 0:
        print("Venda cancelada - Sem troco o suficiente em estoque =(")
        #volta o troco para o original se a venda for cancelada
        changeAvailable = tempChangeAvailable
        return False
    else:
        print("\nTroco:")
        for value in displayChange:
            print(value)
        return True

#MODO ADMIN
#adicionar produtos
def addProduct(stock):
    #criando o array para adicionar na matriz dos produtos com o ID pronto
    array = []
    array.append(len(stock) + 1)
    
    #adicionando o nome do produto
    product_name = input("Digite o nome do produto que você vai adicionar: ")
    array.append(product_name)
    
    #verificação e adição do preço do produto
    while True:
        try:
            product_cost = float(input("Digite o preço do produto: "))
            if product_cost <= 0:
                print("Valor inválido! Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    array.append(int(product_cost * 100))
    
    #verificação e adição do estoque do produto
    while True:
        try:
            stock_quantity = int(input(f"Digite o número de {product_name} que você colocará no estoque: "))
            if stock_quantity <= 0:
                print("Valor inválido! Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
    array.append(stock_quantity)
    #colocando o produto novo do usuário na matriz do estoque
    stock.append(array)
    
    return stock

#editar produtos
def editProduct(stock):
    #garantindo que o ID digitado existe
    while True:
        try:
            product_id = int(input("Digite o ID do produto que gostaria de editar: "))
            validId = False
            #se o id digitado está presente na coluna de IDs da matriz o boolean vira True
            for line in stock:
                if line[0] == product_id:
                    validId = True
            if not validId:
                print("Valor inválido! Digite um ID existente na máquina.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    #alterando o nome do produto desejado
    product_name = input("Digite o novo nome do produto (aperte Enter para manter o atual): ")
    
    #se o usuário digitar algo (diferente de enter) o nome do produto será atualizado
    if product_name:
        stock[product_id - 1][1] = product_name
        
    #atualização do preço seguindo a mesma lógica anterior
    while True:
        try:
            product_cost = input("Digite o novo preço do produto (aperte Enter para manter o atual): ")
            #se o usuário apertar enter, sair da validação
            if not product_cost:
                break
            #transformar o input para float para validar se o preço é maior que 0
            elif float(product_cost) <= 0:
                print("Valor inválido! Digite um número maior que 0.")
                continue
            #se tudo estiver nos conformes, o produto é atualizado
            elif product_cost:
                stock[product_id - 1][2] = int(float(product_cost) * 100)
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
            
    #atualização do estoque seguindo a mesma lógica anterior
    while True:
        try:
            stock_quantity = input("Digite a quantidade de produto que você colocará no estoque (aperte Enter para manter o atual): ")
            #se o usuário apertar enter, sair da validação
            if not stock_quantity:
                break
            #transformar o input para float para validar se o estoque é maior que 0            
            elif int(stock_quantity) <= 0:
                print("Valor inválido! Digite um número maior que 0.")
                continue
            #se tudo estiver nos conformes, o produto é atualizado
            elif stock_quantity:
                stock[product_id - 1][3] = int(stock_quantity)
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
            
    return stock

#remover produtos
def removeProduct(stock):
    #validação do input do usuário para o ID
    while True:
        try:
            product_id = int(input("Digite o ID do produto que gostaria de editar: "))
            #se o id digitado está presente na coluna de IDs da matriz o boolean vira True
            validId = False
            for line in stock:
                if line[0] == product_id:
                    validId = True
            if not validId:
                print("Valor inválido! Digite um ID existente na máquina.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    #remoção do array dentro da matriz com base no ID
    del stock[product_id - 1]
    
    return stock

#modo administrador
def adminMode(stock):
    clear()
    displayStock(stock)
    
    print("\nOpções:\n")
    print("0 - Voltar para a Vending Machine;")
    print("1 - Adicionar produto;")
    print("2 - Editar produto;")
    print("3 - Remover produto\n")
    
    #validação do input do usuário sobre a ação que será executada
    while True:
        try:
            option = int(input("Digite o número da opção que gostaria de executar: "))
            if option >= 0 and option <= 3:
                break
            else:
                print("Valor inválido! Digite um número entre 0 e 3.")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
    
    #mapeamento das ações conforme input
    if option == 0:
        return 0
    elif option == 1:
        stock = addProduct(stock)
    elif option == 2:
        stock = editProduct(stock)
    else:
        stock = removeProduct(stock)
    
    #verificação se o usuário quer voltar pra máquina ou continuar no modo admin
    while True:
        try:
            repeat = int(input("Gostaria de fazer uma nova alteração no modo administrador? Digite 0 para não ou 1 para sim: "))
            if repeat in [0, 1]:
                break
            else:
                print("Valor inválido! Digite 0 ou 1.")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
    
    #se o usuário digitar 1, chamar a função novamente
    if repeat == 1:
        adminMode(stock)
    else:
        return stock

#lista de produtos
productsAvailable = [
    [1, "Coca-cola", 375, 2],    
    [2, "Pepsi", 367, 5],        
    [3, "Monster", 996, 1],      
    [4, "Café", 125, 100],       
    [5, "Redbull", 1399, 2],     
]

#todos os valores em centavos para contornar o problema do ponto flutuante
changeQuantity = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
changeInStock = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
product = checkProduct(productsAvailable, True, True)

while product != 0:
    clear()
    
    #se usuário digitar -1, abrir modo administrador:
    if product == -1:
        adminMode(productsAvailable)
        clear()
        product = checkProduct(productsAvailable, True, True)
    
    if product != 0 and product != -1:
        #valor pago pelo produto e verificação se é válido
        while True:
            try:
                costProduct = float(input(f"O produto custa R${productsAvailable[product-1][2] / 100}. Digite o valor do pagamento: ")) * 100
                costProduct = int(costProduct)
                
                if costProduct < productsAvailable[product-1][2]:
                    print("Valor inválido! O pagamento deve ser maior ou igual ao preço do produto.")
                    continue 
                break 
            except ValueError:
                print("Valor inválido! Digite um número válido.")
        
        #cálculo do troco com base no pagamento
        change = costProduct - productsAvailable[product-1][2]

        possible = calculateChange(change, changeQuantity, changeInStock)
        
        #se a venda for possível, subtrair do estoque e informar o usuário    
        if possible:    
            productsAvailable[product-1][3] -= 1
            print(f"Produto {productsAvailable[product-1][1]} adquirido com sucesso! Restam {productsAvailable[product-1][3]} unidades.\n")
        
        #recomeçar o programa
        product = checkProduct(productsAvailable, True, True)
        
print("\nObrigado por visitar a minha vending machine =)")