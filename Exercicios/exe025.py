#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#Não precisa começar com silva, mas precisa estar em toda a string.

nome = str(input('Digite seu nome: ')).strip()
nome1 = nome.title()
nome1 = 'Silva' in nome1
if nome1 == True:
    print('O nome {} contém o nome Silva!'.format(nome))
else:
    print('Desculpe! Não encontrei Silva no nome digitado.')