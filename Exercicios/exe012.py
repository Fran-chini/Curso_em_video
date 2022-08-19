#Faça um algoritmo que leia o preço de um produto e mostre sua novo preço, com 5% de desconto.

prod = float(input('Qual preço do produto R$'))
nprod = prod - (prod * (5/100))
print('O produto que custava R${:.2f} com desconto de 5% custa R${:.2f}'.format(prod, nprod))