#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a porceção inteira 6
#Obs: Usar Ceil da biblioteca Math

from math import trunc
num = float(input('Digite um número real: '))
print('A parte inteira do valor digitado é {}.'.format(trunc(num)))