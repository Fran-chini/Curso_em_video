'''
Faça um programa para jogar PAR OU ÍMPAR com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.

'''
from random import randrange
from time import sleep
jogador = vitorias = resultado = 0
while True:
    print('-=' * 10)
    print('PAR OU ÍMPAR')
    print('-=' * 10)
    jogador = int(input('Digite um número: '))
    par = ' '
    while par not in 'PIÍ':
        par = str(input('PAR OU ÍMPAR? ')).strip().upper()[0]
    computador = randrange(0, 20)
    print(f'Escolhi {computador}')
    resultado = jogador + computador
    if resultado % 2 == 0:
        if par in 'Pp':
            vitorias += 1
            print('~' * 20)
            print('VOCÊ GANHOU!')
            print('~' * 20)
        else:
            break
    elif resultado % 2 == 1:
        if par in 'IÍií':
            vitorias += 1
            print('~' * 20)
            print('VOCÊ GANHOU!')
            print('~' * 20)
        else:
            break
print('~' * 10)
print('VOCÊ PERDEU!')
print('~' * 10)
print(f'Você ganhou {vitorias} vezes.')
