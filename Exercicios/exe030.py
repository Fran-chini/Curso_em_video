# Crie um programa que leia um número inteiro e mostre se ele é Par ou Impar

n1 = int(input('Digite um número: '))
resp = n1 % 2
if resp == 0:
    print('O número {} é Par!'.format(n1))
else:
    print('O número {} é Impar!'.format(n1))