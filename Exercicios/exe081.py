'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados
B) A lista de valores, ordenados de forma decrescente
C) Se o valor 5 foi digitado e se está ou não na lista

'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    sair = str(input('Deseja continuar?[S/N] ')).strip().lower()[0]
    if sair in "Nn":
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} números')
print(f'A lista em ordem descrente seria {lista}')
if 5 in lista:
    print('O número 5 foi digitado e imputado na lista.')
else:
    print('O número 5 não foi digitado!')
