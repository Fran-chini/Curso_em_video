'''
Crie um programa que tenha uma túpla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''
#SOLUÇÃO GUANABARA
listaMercado = ('Leite', 7.00,
                'Café', 27.00,
                'Margarina', 7.00,
                'Pão Frances', 17.00)
for pos in range(0, len(listaMercado)):
    if pos % 2 == 0:
        print(f'{listaMercado[pos]:.<30}', end='')
    else:
        print(f'R${listaMercado[pos]:>7.2f}')

