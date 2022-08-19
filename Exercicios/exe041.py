'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento
 de um atleta e mostre sua categoria, de acordo com a idade:

 - Até 9 anos: MIRIM
 - Até 14 anos: INFANTIL
 - Até 19 anos: JUNIOR
 - Até 20 anos: SENIOR
 - Acima: MASTER'''
from datetime import date
ano_nascimento = int(input('Qual a sua idade: '))
idade = abs(ano_nascimento - date.today().year)
if ano_nascimento <= 9:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Mirim')
elif 9 < ano_nascimento <= 14:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Infantil')
elif 14 < ano_nascimento <= 19:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Junior')
elif 19 < ano_nascimento <= 20:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Senior')
else:
    print('O atleta tem {} anos'.format(idade))
    print('Classificação: Master')


