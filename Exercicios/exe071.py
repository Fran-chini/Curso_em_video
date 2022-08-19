'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas células
de cada valor serão entregues.

Considere que o caixa possui células de R$50, R$20, R$10 e R$1


'''
nota50 = nota20 = nota10 = nota1 = resto = 0
while True:
    valor = int(input('Deseja sacar qual valor ? R$'))
    nota50 = int(valor / 50)
    valor = valor - (nota50 * 50)
    nota20 = int(valor / 20)
    valor = valor - (nota20 * 20)
    nota10 = int(valor / 10)
    valor = valor - (nota10 * 10)
    nota1 = int(valor / 1)
    valor = valor - (nota1 * 1)
    if nota50 > 0:
        print(f'Você terá {nota50:.0f} notas de R$50,00')
    if nota20 > 0:
        print(f'Você terá {nota20:.0f} notas de R$20,00')
    if nota10 > 0:
        print(f'Você terá {nota10:.0f} notas de R$10,00')
    if nota1 > 0:
        print(f'Você terá {nota1:.0f} notas de R$1,00')
    if valor == 0:
        break


