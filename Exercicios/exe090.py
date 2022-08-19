# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# >7 = Aprovado

sitAluno = dict()
sitAluno['Nome'] = str(input('Qual o nome do(a) aluno(a): '))
sitAluno['Media'] = float(input(f'Qual a média do aluno(a) {sitAluno["Nome"]}: '))
if sitAluno['Media'] >= 7:
    sitAluno['Situação'] = 'Aprovado'
else:
    sitAluno['Situação'] = 'Reprovado'

print(f'Nome é igual a {sitAluno["Nome"]}')
print(f'Média é igual á {sitAluno["Media"]}')
print(f'Situação é igual á {sitAluno["Situação"]}')


