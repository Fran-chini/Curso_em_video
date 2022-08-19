'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

import random
from time import sleep
listSort = list()
c = 0
for c in range(1, 61):
    listSort.append(c)
print('-'*40)
print('{:^38}'.format('JOGA NA MEGA SENA'))
print('-'*40)
v = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, v+1):
    jogo = random.sample(listSort, 6)
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    sleep(1)
