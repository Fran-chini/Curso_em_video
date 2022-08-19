#Crie um programa que leia o nome de uma pessoa e mostre
# 1 - O nome com todas as letras maiúsculas ✔
# 2 - O nome com todas as letras minúsculas  ✔
# 3 - Quantas letras tem ao todo sem contar os espaços
# 4 - Quantas letras tem o primeiro nome

nome = str(input('Qual o seu nome completo: '))
print('Seu nome com todas as letras maiúsculas {}'.format(nome.upper()))
print('Seu com todas as letras minísculas {}'.format(nome.lower()))
novo_nome = nome.split()
novo_nome_1 = ''.join(novo_nome)
print('Sem contar os espaços seu nome contém {} letras'.format(len(novo_nome_1)))
print('O seu primeiro nome contém {} letras'.format(len(novo_nome[0])))

