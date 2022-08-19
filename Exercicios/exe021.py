#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
#Obs: Procurar bibliotecas que tenham a função de reproduzir.
import pygame

pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
input()


