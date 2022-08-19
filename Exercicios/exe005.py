#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e antecessor
n1 = int(input('Digite um número: '))
ant = n1 - 1
suce = n1 + 1
print('O antecessor de {} é {}.\nO sucessor de {} é {}.'.format(n1, ant, n1, suce))
