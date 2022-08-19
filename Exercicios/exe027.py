#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

#Ex Ana Maria de Souza
# Primeiro Nome: Ana
# Último NOme: Souza
#Independente do tamanho do nome.

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.title()
nome1 = nome1.split()
ultnome = int(len(nome1)) - 1
print('Primeiro nome: {}'.format(nome1[0]))
print('Último nome: {}'.format(nome1[ultnome]))
