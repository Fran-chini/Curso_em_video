#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usauário venceu ou perdeu!
from random import randrange
from time import sleep
print('*' * 50)
print('|{:^48}|'.format('JOGO DA ADIVINHAÇÃO 1.0'))
print('*' * 50)
print('|{:^48}|'.format('PENSANDO EM UM NÚMERO...'))
print('-' * 50)
sleep(4)
numero = randrange(0, 5)
print('|{:^48}|'.format('ENCONTREI UM NÚMERO ENTRE 0 E 5'))
print('-' * 50)
resp = int(input('Qual número eu pensei? '))
if resp == numero:
    print('Você VENCEU!, eu escolhi {}.'.format(numero))
else:
    print('GAME OVER! Escolhi {}, tente novamente!'.format(numero))
print('-' * 50)
print('|{:^48}|'.format('FIM DO JOGO!'))
print('-' * 50)


