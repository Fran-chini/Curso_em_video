'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

'''
pa = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão da PA? '))
decimo = pa + (10 - 1) * r
for c in range(pa, decimo + r, r):
    print(pa, end=" → ")
    pa += r
print('Acabou!')

