'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior Número
[4] Novos Números
[5] Sair do Programa

Seu programa deverá realizar operação solicitada em cada opção

'''
'''menu = 0
while menu != 5:
    n1 = float(input('Digite 1º número: '))
    n2 = float(input('Digite 2º número: '))
    print(Qual operação deseja fazer? 
[1] Somar
[2] Multiplicar
[3] Maior Número
[4] Novos Números
[5] Fechar Programa)
    menu = int(input('Digite uma opção: '))
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} = {}.'.format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n1))
        else:
            print('O maior número entre {} e {} é {}.'.format(n1, n2, n2))
    elif menu == 4:
            print('Digite os novos números: ')
            n1 = float(input('Digite 1º número: '))
            n2 = float(input('Digite 2º número: '))
    elif menu == 5:
        print('Fim de Operação!')
    else:
        print('Opção Inválida!')'''

#------RESPOSTA GUANABARA--------#
from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 5:
    sleep(2)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior Número
    [4] Novos Números
    [5] Fechar Programa''')
    opção = int(input('Qual sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Digites os novos valores!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        print('Finalizando!')
    else:
        print('Opção Inválida. Tente novamente')
    print('-=' * 10)


print('Fim do programa. Volte sempre!')

