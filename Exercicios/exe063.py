'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
sequencia de fibonacci

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8...até N

'''

n = int(input('Deseja ver quantas sequência de Fibonacci? '))
termo = 0
ultimo = 1
penultimo = 1
c = 0
while c != n:
    if 0 == c:
        print(0, end=' - ')
        c += 1
    if c == 1 or c == 2:
        print(1, end=' - ')
        c += 1
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(termo, end=' - ')
        c += 1
print('Acabou!')



