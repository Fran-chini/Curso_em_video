'''
Crie um programa que o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta(Sem usar o sort()).

no final, mostre a lista ordenada na tela.

'''
numeros = []
ordemDigitada = []
num = int(input('Digite um valor: '))
numeros.append(num)
ordemDigitada.append(num)
print(f'O número {num} foi adicionado no final da lista.')
for c in range(4):
    num = int(input(f'Digite um valor: '))
    if num >= max(numeros):
        numeros.append(num)
        ordemDigitada.append(num)
        print(f'O número {num} foi adicionado no final da lista.')
    elif num <= min(numeros):
        numeros.insert(0, num)
        ordemDigitada.append(num)
        print(f'O número {num} foi adicionado na posição 0 da lista.')
    elif num > min(numeros) < max(numeros):
        if num > numeros[1]:
            numeros.insert(2, num)
            ordemDigitada.append(num)
            print(f'O número {num} foi adicionado na posição 2 da lista.')
        else:
            numeros.insert(1, num)
            ordemDigitada.append(num)
            print(f'O número {num} foi adicionado na posição 1 da lista.')
print(f'Você digitou os números {ordemDigitada}')
print(f'Sua lista em ordem crescente é {numeros}')
