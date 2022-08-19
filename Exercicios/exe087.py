'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

'''lista1 = list()
info = list()
c = tot3c = somapares = maiorvalor = totpar = 0
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
print(lista1[6], lista1[7], lista1[8])
for v in lista1:
    if v[0] % 2 == 0:
        totpar += v[0]
total3c = lista1[6] + lista1[7] + lista1[8]
maiorvalor = lista1[3] + lista1[4] + lista1[5]
print(f'O total dos valores pares é {totpar}')
print(f'A soma total da terceira coluna é {sum(total3c)}')
print(f'O maior valor digitado na segunda linha é {max(maiorvalor)}')'''

#Resposta Guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior elemento da segunda linha é {mai}')
























