# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

viagem = float(input('Qual a quantos Km rodou: '))
if viagem <= 200:
    pas = viagem * 0.5
    print('Seu viagem é menor que 200km!')
   # print('O valor da passagem é R${:.2f}'.format(pas))
else:
    pas = viagem * 0.45
    print('Sua viagem é maior que 200km')
    #print('Sua passagem ficará no valor de R${:.2f}'.format(pas))
print('Sua passagem ficará no valor de R${:.2f}'.format(pas))