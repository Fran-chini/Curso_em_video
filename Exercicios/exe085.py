'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
'''
'''lista1 = list()
pares = list()
impares = list()
for c in range(7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
lista1.append(pares)
lista1.append(impares)
print(f'Os números pares são {lista1[0]}')
print(f'Os números ímpares são {lista1[1]}')'''


#Resposta Guanabara

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'OS valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')



















