'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamenteaté ter um valor caorreto.

'''
sexo = ''
while 'M' != sexo != 'F':
    sexo = str(input('Qual sexo? [M/F]')).strip().upper()
    if 'm' != sexo != 'f':
        print('Sexo Inválido!\nDigite novamente.')
print('Sexo {} cadastrado com sucesso!'.format(sexo))