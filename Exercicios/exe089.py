'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.'''
#from tabulate import tabulate
cadastro = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])
    sim = str(input('Deseja cadastrar outro aluno? [S/N]')).strip()[0]
    while sim not in 'SsNn':
        print('Opção Inválida! Tente novamente.')
        sim = str(input('Deseja cadastrar outro aluno? [S/N]')).strip()[0]
    if sim in 'Nn':
        break
print('-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print(f'{"-"*9}{"Fim da lista":^12}{"-"*9}')
while True:
    print('-'*30)
    print(f'{"I"}{"Consultar notas":^28}{"I"}')
    print('-'*30)

    opc = int(input('Escolha o indice do aluno para ver a nota: (999 para sair) '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(cadastro)-1:
        print(f'As notas do aluno {cadastro[opc][0]} são {cadastro[opc][1]}')
print('-'*30)
print(f'{"I"}{"Volte sempre":^28}{"I"}')
print('-'*30)

