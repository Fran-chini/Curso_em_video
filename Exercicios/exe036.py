'''Escreva um programa para aprovar um emprestimo bancário,
para a compra de um imóvel. O programa vai perguntar o valor da casa,
o valor do salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exeder 30%
do salário ou então o emprestimo será negado.'''
from math import ceil

print('\033[34m-=\033[m' * 20)
print('\033[34m|\033[m{:^38}\033[34m|\033[m'.format('EMPRESTIMO BANCÁRIO'))
print('\033[34m-=\033[m' * 20)

casa = float(input('Qual o valor do Imóvel R$'))
salario = float(input('Qual o seu salário R$'))
anos = int(input('Quantos anos deseja pagar o empréstimo? '))
anos = anos * 12
limite = salario * 30 / 100  # Calcula o valor de 30% do salario do comprador
aprovado = casa / anos  # Valor de parcela que o comprador solicitou
tcerto = (casa / limite)

if aprovado <= limite:
    print('\033[33m-=\033[m' * 20)
    print('\033[33m|\033[m{:^38}\033[33m|\033[m'.format('FINANCIAMENTO APROVADO!'))
    print('\033[33m-=\033[m' * 20)
    print('O valor da prestação ficou em \033[32mR${:.2f}\033[m'.format(aprovado))
else:
    print('\033[31m-=\033[m' * 20)
    print('\033[31m|\033[m{:^38}\033[31m|\033[m'.format('FINANCIAMENTO REPROVADO!'))
    print('\033[31m|\033[m{:^38}\033[31m|\033[m'.format('Parcela ultrapassa 30% do salário!'))
    print('\033[31m|\033[m{:^38}\033[31m|\033[m'.format('Sugira o prazo de:'))
    print('\033[31m|\033[m{:^38}\033[31m|\033[m'.format(ceil(tcerto)))
    print('\033[31m|\033[m{:^38}\033[31m|\033[m'.format('Vezes'))
    print('\033[31m-=\033[m' * 20)

print('\033[34m-=\033[m' * 20)
print('\033[34m|\033[m{:^38}\033[34m|\033[m'.format('FIM DE NOGOCIAÇÃO'))
print('\033[34m-=\033[m' * 20)
