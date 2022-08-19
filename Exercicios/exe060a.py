'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex:

5! = 5x4x3x2x1 = 120

'''
#----------RESPOSTA DO GUANABARA------------#
n = int(input('Digite um número para ver o seu Fatorial: '))
c = n
f = 1
print('O fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    f *= c
    c -= 1
    print(' x ' if c >= 1 else ' = ', end='' )
print('{}'.format(f), end='')