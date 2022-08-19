'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar.

No final mostre:

A) Quantas pessoas tem mais de 18 anos. ✔
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos✔

'''
from time import sleep
maior18 = menor20 = homens = 0
NomeApp = 'Cadastros de pessoas'
while True:
    print('-' * 30)
    print(f'|{NomeApp:^28}|')
    print('-' * 30)
    sexo = ' '
    idade = int(input('Qual a sua idade: '))
    while sexo not in 'MF':
        sexo = str(input('Qual sexo: [M/F] ')).strip().upper()[0]
        if idade > 18:
            maior18 += 1
            print('Cadastro realizado com sucesso!')
        if idade < 20 and sexo == 'F':
            menor20 += 1
            print('Cadastro realizado com sucesso!')
        if sexo == 'M':
            homens += 1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if sair == 'N':
        break
print('Armazenando cadastros...')
sleep(1)
print(f'Mais de {maior18} pessoas são maiores de 18 anos.')
sleep(1)
print(f'Foram cadastrados {homens} homens no sistema.')
sleep(1)
print(f'{menor20} mulheres são menores de 20 anos.')
print('Fim de execução.')

