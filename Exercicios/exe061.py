'''
Refaça o desafio 51, lendo o primeiro termo e a raão de uma PA, mostrando os 10 primeiros termos
da progressão usando While

"A fórmula do termo geral da progressão aritmética é a seguinte:

an = a1 + (n – 1) * r

'''

pa = int(input('Qual é o termo da PA? '))
r = int(input('Qual é a razão da PA? '))
decimo = pa + (10 - 1) * r
c = 0
while c != 10:
    for c in range(pa, decimo + r, r):
        pa += r
        print(pa, end='')
        print(' → ' if c < decimo else '', end='')
print('Acabou!')
