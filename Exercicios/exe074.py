'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


'''
from random import randint
'''lista1 = (randint(1, 10))
lista2 = (randint(1, 10))
lista3 = (randint(1, 10))
lista4 = (randint(1, 10))
lista5 = (randint(1, 10))
listaFinal = lista1 + lista2 + lista3 + lista4 + lista5'''
#GUANABARA
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados são: ', end='')
'''maior = sorted(listaFinal)
print(f'O maior número foi {maior[-1]}\nO menor número foi {maior[-5]}')'''
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')


