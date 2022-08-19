'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- A vista DINHEIRO/CHEQUE: 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no carão: 20% de juros'''

from time import sleep
loja = 'LOJA DO REAL'
valor = float(input('Qual o valor do produto R$'))
print('\033[33m-\033[m' * 40)
print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format(loja))
print('\033[33m-\033[m' * 40)
print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('Buscando formas de pagamento...'))
sleep(3)
print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('Escolha a opção de pagamento abaixo'))
print('\033[33m|\033[m\033[30m[1] Dinheiro/Cheque\033[m\n\033[33m|\033[m\033[30m[2] Á Vista no Cartão\033[m\n\033[33m|\033[m\033[30m[3] 2x No Cartão\033[m\n\033[33m|\033[m\033[30m[4] 3x ou mais no Cartão\033[m')
opcao = int(input('\033[33m|\033[m\033[30mEscolha a opção de pagamento:\033[m '))
print('\033[33m-\033[m' * 40)


if opcao == 1:
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('PAGAMENTO EM DINHEIRO/CHEQUE'))
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('10% de Desconto'))
    print('\033[33m-\033[m' * 40)
    print('O produto custa R${:.2f}'.format(valor))
    desc = valor * 10 / 100
    valor = valor - valor * 10 / 100
    print('Com desconto de R${:.2f}\nO Produto saíra á R${:.2f}'.format(desc, valor))
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('TOTAL A RECEBER'))
    print('\033[33m|\033[m\033[30m{:^38.2f}\033[m\033[33m|\033[m'.format(valor))

elif opcao == 2:
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('PAGAMENTO EM Á VISTA NO CARTÃO'))
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('5% de Desconto'))
    print('\033[33m-\033[m' * 40)
    print('O produto custa R${:.2f}'.format(valor))
    desc = valor * 10 / 100
    valor = valor - valor * 5 / 100
    print('Com desconto de R${:.2f}\nO Produto saíra á R${:.2f}'.format(desc, valor))
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('TOTAL A RECEBER'))
    print('\033[33m|\033[m\033[30m{:^38.2f}\033[m\033[33m|\033[m'.format(valor))
elif opcao == 3:
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('PAGAMENTO EM 2x CARTÃO'))
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('SEM DESCONTO'))
    print('\033[33m-\033[m' * 40)
    print('O produto custa R${:.2f}'.format(valor))
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('TOTAL A RECEBER'))
    print('\033[33m|\033[m\033[30m{:^38.2f}\033[m\033[33m|\033[m'.format(valor))
else:
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('PAGAMENTO EM 3x OU MAIS'))
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('20% DE JUROS'))
    print('\033[33m-\033[m' * 40)
    vezes = int(input('Quantas vezes? '))
    print('O produto custa R${:.2f}'.format(valor))
    juros = valor * 20 / 100
    valor = valor + valor * 20 / 100
    parcela = valor / vezes
    print('Com juros de R${:.2f}\nO Produto saíra á R${:.2f}'.format(juros, valor))
    print('Parcelado em {}x, pagará parcelas no valor de R${:.2f}'.format(vezes, parcela))
    print('\033[33m-\033[m' * 40)
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('TOTAL A RECEBER'))
    print('\033[33m|\033[m\033[30m{:^38.2f}\033[m\033[33m|\033[m'.format(valor))
    print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('TOTAL POR PARCELA'))
    print('\033[33m|\033[m\033[30m{:^38.2f}\033[m\033[33m|\033[m'.format(parcela))

print('\033[33m-\033[m' * 40)
print('\033[33m|\033[m\033[30m{:^38}\033[m\033[33m|\033[m'.format('FIM DE PROCESSO'))
print('\033[33m-\033[m' * 40)
