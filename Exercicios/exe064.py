'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usúario digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (Desconsiderando o flag)

'''
cont = soma = 0
n = int(input('Digite um número inteiro ou 999 para sair: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro ou 999 para sair: '))
print('Você digitou {} números.\nA soma dos números são {}.'.format(cont, soma))
