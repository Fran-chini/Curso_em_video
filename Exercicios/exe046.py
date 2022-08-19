'''
Faça um programa que mostre uma contagem regressiva na tela para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles

OBS: Usar biblioteca time (sleep)
OBS: Usar Iterador -1 no looping de FOR
'''

from time import sleep
import emoji


for c in range(10, -1, -1): #Para o contador que começa em 10 e vai até -1 pulando de -1 em -1
    sleep(1) #Tempo de exibição 1 segundo
    print(c) #exibir o contador
print(emoji.emojize(":fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:", language="alias"))#fogos de artifícios
