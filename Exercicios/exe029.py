# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 por cada Km acima do limite
import pygame
from time import sleep
velo = float(input('Qual a volocidade do carro? '))
print('-' * 50)
print('|{:^48}|'.format('ANALISANDO SUA VELOCIDADE...'))
print('-' * 50)
sleep(2)
if velo > 80:
    multa = float((velo - 80) * 7)
    print('-' * 50)
    print('|{:^48}|'.format('ATENÇÃO! VOCÊ FOI MULTADO!'))
    print('-' * 50)
    print('Você estava a {} Km/h acima da velocidade!'.format(velo - 80))
    print('-' * 50)
    print('|{:^48}|'.format('MULTA DE R$'))
    print('|{:^48.2f}|'.format(multa))
    print('-' * 50)
    pygame.init()
    pygame.mixer.music.load('policia.mp3.mp3')
    pygame.mixer.music.play()
    input('PRESSIONE UMA TECLA PARA FINALIZAR!')
else:
    print('-' * 50)
    print('|{:^48}|'.format('PARABÉNS! Você está na velocidade correta!'))
    print('-' * 50)
    pygame.init()
    pygame.mixer.music.load('aplausos.mp3')
    pygame.mixer.music.play()
    input('PRESSIONE UMA TECLA PARA FINALIZAR!')
print('-' * 50)
print('|{:^48}|'.format('ANALISE FINALIZADA!'))
print('-' * 50)
