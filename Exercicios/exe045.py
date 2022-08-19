'''Crie um programa que faça o computador jogar JOKENPÔ com você'''

import random
import time
import emoji
rodada = 0
pontos_pc = 0
pontos_usuario = 0
while rodada < 3:
    pedra = 0
    papel = 1
    tesoura = 2
    placar_pc = 0
    placar_usuario = 0
    pc = random.randint(0, 2)
    print('-=' * 15)
    print('|{:^28}|'.format('JOKEMPÔ'))
    print('|{:^28}|'.format('PEDRA, PAPEL, TESOURA'))
    print('-=' * 15)
    print('Vamos começar...')
    print(emoji.emojize("Pedra :facepunch:", language="alias"))
    time.sleep(2)
    print(emoji.emojize("Papel :hand:", language="alias"))
    time.sleep(2)
    print(emoji.emojize("Tesoura :v:", language="alias"))
    usuario = input('Qual você escolhe: ').strip().lower()
#PARTE LÓGICA DO JOGO
    if usuario == 'pedra':
        if pc == pedra:
            print(emoji.emojize("Escolhi :facepunch:", language="alias"))
            print('Jogo Empatou!')
        elif pc == papel:
            print(emoji.emojize("Escolhi :hand:", language="alias"))
            print('GANHEI!!')
            placar_pc = 1
        else:
            print(emoji.emojize("Escolhi :v:", language="alias"))
            print('Você GANHOU!')
            placar_usuario = 1
    elif usuario == 'papel':
        if pc == papel:
            print(emoji.emojize("Escolhi :hand:", language="alias"))
            print('Jogo Empatou!')
        elif pc == tesoura:
            print(emoji.emojize("Escolhi :v:", language="alias"))
            print('GANHEI!!')
            placar_pc = 1
        else:
            print(emoji.emojize("Escolhi :facepunch:", language="alias"))
            print('Você GANHOU!')
            placar_usuario = 1
    elif usuario == 'tesoura':
        if pc == tesoura:
            print(emoji.emojize("Escolhi :v:", language="alias"))
            print('Jogo Empatou!')
        elif pc == pedra:
            print(emoji.emojize("Escolhi :facepunch:", language="alias"))
            print('GANHEI!!')
            placar_pc = 1
        else:
            print(emoji.emojize("Escolhi :hand:", language="alias"))
            print('Você GANHOU!')
            placar_usuario = 1
    else:
        print('Algo deu errado!\nMotivo 1 - Digitou errado!\nMotivo 2 - ErrorAlgoritmo\nReinicie o jogo!')
    rodada += 1
#CONTADOR DE PONTOS
    if placar_pc == 1:
        pontos_pc += placar_pc
    else:
        pontos_usuario += placar_usuario
    print('-=' * 15)
    print('|{:^28}|'.format('PLACAR ATUAL'))
    print('-=' * 15)
    print('Computador {} x {} Usuário'.format(pontos_pc, pontos_usuario))
if pontos_pc > pontos_usuario:
    print(emoji.emojize("Máquina Ganhou, boa sorte na próxima! :fire::fire::fire:", language="alias"))
elif pontos_pc == pontos_usuario:
    print(emoji.emojize("O jogo empatou ! :triumph::triumph::triumph:", language="alias"))
else:
    print(emoji.emojize("VOCÊ GANHOU ! Parabéns :clap::clap::clap::clap:", language="alias"))




