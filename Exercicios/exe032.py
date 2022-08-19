# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
#Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4,
# deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;

#Segunda situação: Se o ano de 2015 ou 2016 não for divisível por 4,
# então deveremos verificar se ele é divisível por 400. Se também não for divisível,
# o ano de 2015 não será bissexto;

#Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4,
# então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.

ano = int(input('Digite o Ano: '))
Primeira_Situação = ano % 4
Primeira_Situação1 = ano % 100
Primeira_Stuação2 = ano % 400
if Primeira_Situação == 0 and Primeira_Situação1 != 0 or Primeira_Stuação2 == 0:
    print('O ano de {} é Bissexto e Fevereiro terá 29 dias.'.format(ano))
else:
    print('O ano de {} não é Bissexto e Fevereiro terá 28 dias.'.format(ano))

