'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:

5! = 5x4x3x2x1 = 120

'''

fat = int(input('Qual número deseja ver o fatorial? '))
c = 0
fatorial = fat
while c != 1:
    for c in range(fat, 1, -1):
        c -= 1
        fat = fat * c
print('O fatorial de {}! é {}.'.format(fatorial, fat))
