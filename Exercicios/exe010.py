#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela
#pode comprar.
#Considere US$1,00 == R$3,27
dol = float(4.73)
print('-'*60)
print('|{:^58}|'.format('CONVERTA SEU DINHEIRO EM DÓLAR COTAÇÃO ATUAL US${:.2f}'.format(dol)))
print('-'*60)
real = float(input('Quantos Reais você tem R$'))
resp = real / dol
print('Convertendo R${:.2f} para Dólar, terá US${:.2f}'.format(real, resp))
print('-'*60)
print('|{:^58}|'.format('VALOR CONVERTIDO!'))
print('-'*60)