'''
Crie um programa que leia o ano de nascimento de sete pessoas.

No final mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maior.

'''
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for c in range(7):
    ano = int(input('Digite o {}º ano de nascimento: '.format(c+1)))
    idade = abs(ano - ano_atual)
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maiores de idade!\n{} pessoas são menores de idade.'.format(maior, menor))

