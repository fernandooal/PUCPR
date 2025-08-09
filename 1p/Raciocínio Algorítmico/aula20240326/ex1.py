'''
1) Implemente um programa em Python para ler do teclado a
nota de um aluno. Verifique se o valor lido é uma nota válida
(maior que 7). Se não for, ler este valor até que a mesma seja
válida.
'''

nota = float(input("Digite a nota do aluno: "))

while(nota < 7):
    nota = float(input("Nota inválida! Insira um valor acima de 7: "))

print("Nota válida!")