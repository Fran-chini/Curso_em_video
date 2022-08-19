'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes aparece o valor 9.✔
B) Em que posição foi digitado o primeiro valor 3✔
C) Quais foram os números pares
'''
'''lista1 = ()
lista2 = ()
lista3 = ()
lista4 = ()
pares = []
nove = 0
for c in range(1, 5):
    num = int(input('Digite um número: '))
    if c == 1:
        lista1 = str(num)
        if num == 9:
            nove += 1
        if num % 2 == 0:
            pares.append(num)
    elif c == 2:
        lista2 = str(num)
        if num == 9:
            nove += 1
        if num % 2 == 0:
            pares.append(num)
    elif c == 3:
        lista3 = str(num)
        if num == 9:
            nove += 1
        if num % 2 == 0:
            pares.append(num)
    elif c == 4:
        lista4 = str(num)
        if num == 9:
            nove += 1
        if num % 2 == 0:
            pares.append(num)
listaGeral = lista1 + lista2 + lista3 + lista4
print(f'Foram digitados {nove} números 9.')
if "3" in listaGeral:
    print(f'O número 3 aparece primeiro na posição {listaGeral.index("3")+1}')
else:
    print('Número 3 não foi adicionado a lista!')
print(f'Os números pares digitados foram {pares}')'''

#GUANABARA

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os números {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitando em nenhuma posição!')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

