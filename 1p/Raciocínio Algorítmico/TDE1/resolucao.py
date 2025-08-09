import math

#1. Faça um algoritmo que leia um número inteiro e escreva seu antecessor e sucesso.
numero = int(input("Digite um número inteiro: "))

print(f"O antecessor do número digitado é {numero-1} e o sucessor é {numero+1}")

#2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade que completará em 2022.
anoNasc = int(input("Digite o ano do seu nascimento: "))

print(f"Você completou {2022-anoNasc} em 2022!")

#3. Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.
salario = float(input("Digite seu salário: "))

print(f"Você recebe {salario/1412} salários mínimos.")

#4. Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
#(1) a vista com 5% de desconto; (2) o valor da parcela em 2x; (3) o valor da parcela em 3x com acréscimo de 5%.
valorProduto = float(input("Digite o valor do produto desejado: "))

print(f"À vista: {valorProduto*0.95}; Parcela em 2x: {valorProduto/2}; Parcela em 3x: {(valorProduto*1.05)/3}")

#5. Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l), solicitando como entrada a distância 
#total percorrida (KM) e o volume de combustível consumido para percorre-la (litros).
distancia = float(input("Digite quantos quilômetros você andou: "))
combustivel = float(input("Digite quantos litros de gasolina você usou nessa viagem: "))

print(f"O consumo médio de combustível foi de {distancia/combustivel}km/l")

#6. Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar
#um tanque cilindro, em que são fornecidas sua altura e raio, sabendo que:
#a. A lata de tinta custa R$ 50,00
#b. Cada lata contém 5 litros
#c. Cada litro de tinta pinta 3 metros quadrados
#d. Entrada do programa: altura e raio do cilindro
#e. Saída: valor em reais e quantidade de latas

altura = float(input("Digite a altura do tanque em metros: "))
raio = float(input("Digite o raio do tanque em metros: "))

areaTanque = (2*3.14*raio*altura)+(2*3.14*(raio**2))
qntdLatas = (areaTanque/3)/5

print(f"Você precisará de {math.ceil(qntdLatas)} latas de tinta, que equivale a {round((qntdLatas*50), 2)} reais.")