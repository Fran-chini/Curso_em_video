'''
Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.

Exercicio 28:

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 10
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usauário venceu ou perdeu!
'''

from random import randint
from time import sleep

computador = 0
palpites = 0
jogador = 1
print('\033[36m-=\033[m' * 15)
print('\033[36m|{:^28}|\033[m'.format('JOGO DA ADIVINHAÇÃO 2.0'))
print('\033[36m-=\033[m' * 15)
print('PENSANDO EM UM NÚMERO', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('PENSEI! TENTE ACERTAR!!!')
computador = randint(0, 10)
acertou = False
jogador = int(input('Qual seu palpite? '))
while not acertou:
    palpites += 1
    if computador == jogador:
        acertou = True
    if jogador < computador:
        jogador = int(input('Mais...Qual Seu palpite?'))
    elif jogador > computador:
        jogador = int(input('Menos...Qual Seu palpite? '))
print('\033[35m-=\033[m' * 15)
print('\033[35m|{:^28}|\033[m'.format('AEEEE, VOCÊ GANHOU!!'))
print('\033[35m-=\033[m' * 15)
print('Para ganhar você precisou de {} palpites.'.format(palpites))



