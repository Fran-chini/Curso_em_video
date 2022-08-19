'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

'''
from tabulate import tabulate

'''lista1 = list()
info = list()
c = 0
while c < 3:
    info.append(int(input(f'Digite um número na posição [0, {c}]')))
    lista1.append(info[:])
    info.clear()
    c += 1
c = 0
while c < 3:
    info.append(int(input(f'Digite um número na posição [1, {c}]')))
    lista1.append(info[:])
    info.clear()
    c += 1
c = 0
while c < 3:
    info.append(int(input(f'Digite um número na posição [2, {c}]')))
    lista1.append(info[:])
    info.clear()
    c += 1
print(lista1[0], lista1[1], lista1[2])
print(lista1[3], lista1[4], lista1[5])
print(lista1[6], lista1[7], lista1[8])'''


#resposta guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
























