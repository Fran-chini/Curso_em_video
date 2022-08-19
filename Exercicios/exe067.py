'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

'''
from time import sleep
n = cont = 0
while True:
    print('Digite um número negativo para sair!')
    n = int(input('Deseja ver a tabuada de qual número?'))
    if n < 0:
        break
    print('-=' * 10)
    print(f'Tabuada do {n}')
    print('-=' * 10)
    sleep(2)
    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n * cont:2}')
print('Fim de execução!')


