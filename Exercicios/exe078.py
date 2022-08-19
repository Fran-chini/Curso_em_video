'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respsectivas posições na lista.


'''
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º número na posição {c}: ')))
print(f'Você digitou os números {valores}.')
print(f'O maior número digitado {max(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(c, end='... ')
print(f'\nO menor número digitado foi {min(valores)} nas posições ', end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(c, end='... ')


