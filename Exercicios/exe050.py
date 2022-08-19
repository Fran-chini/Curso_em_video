'''
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem pares.
Se o valor for Ímpar, desconsidere-o

'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares.\nA soma dos números pares são {}'.format(cont, soma))