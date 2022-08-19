'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar.

No final, mostre:

A) Qual o total gasto na compra ✔
B) Quantos produtos custam mais de R$1000✔
C) Qual é o nome do produto mais barato

'''
comercio = 'LOJA DO REAL CEV'
TotGasto = maisdemil = EmConta = cont = 0
barato = ''
while True:
    print('※' * 20)
    print(f'※{comercio:^29}※')
    print('※' * 20)
    produto = str(input('Qual produto? ')).strip().upper()
    preço = float(input('Qual o preço? R$'))
    TotGasto += preço
    cont += 1
    if preço > 1000:
        maisdemil += 1
    if cont == 1:
        barato = produto
        EmConta = preço
    elif preço < EmConta:
        barato = produto
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print(f'O total da compra ficou em R${TotGasto}')
print(f'{maisdemil} produtos custam mais de R$1000,00')
print(f'O produto mais barato em sua compra foi {barato}.')
