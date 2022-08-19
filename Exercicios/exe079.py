'''
Criei um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
já axista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.

'''
variosNumeros = []
n = ''
while True:
    num = int(input('Digite um número: '))
    while num in variosNumeros:
        print('Valor já cadastrado!\nTente novamente!')
        num = int(input('Digite um número: '))
    variosNumeros.append(num)
    print(f'Valor {num} cadastrado com sucesso!')
    resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Os números cadastrados foram: ', end='')
for c, n in enumerate(sorted(variosNumeros)):
    print(n, end='... ')
print('\nFim do programa!')
