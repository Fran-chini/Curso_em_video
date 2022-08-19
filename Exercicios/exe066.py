'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição
de parada(flag(bandeira)). No final mostre quantos números foram digitadose qual foi a soma
entre eles(desconsiderando o flag)

'''

numeros = soma = 0
while True:
    n = int(input('Digite um número[999 para sair]: '))
    if n == 999:
        break
    numeros += 1
    soma += n
print(f'Você digitou {numeros} números e a soma de todos foram {soma}.')