'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas. ✔
B) Uma listagem com as pessoas mais pesadas(Considrando 100kg o mais pesado)✔✔
C) Uma listagem com as pessoas mais leves.✔✔✔
'''
dados = list()
pessoas = list()
pessPesado = list()
pessLeve = list()
peso = list()
qtdPessoas = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    qtdPessoas += 1
    dados.append(float(input('Peso: ')))
    peso.append(dados[1])
    pessoas.append(dados[:])
    dados.clear()
    sair = str(input('Deseja continuar?[S/N] ').strip())
    if sair in 'Nn':
        break
print(f'Dados cadastrados: {pessoas}')
print(f'Ao todo, foram cadastrados {qtdPessoas} pessoas.')
for p in pessoas:
    if p[1] == max(peso):
        pessPesado.append(p[0])
    if p[1] == min(peso):
        pessLeve.append(p[0])
print(f'As pessoas com os maiores pesos são {pessPesado} com {max(peso):.2f}Kg')
print(f'As pessoas com os menores pesos são {pessLeve} com {min(peso):.2f}Kg')
