'''
Crie um programa que vai ler vários vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
impares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas

'''
listaGeral = []
pares = []
impares = []
while True:
    listaGeral.append(int(input('Digite um número: ')))
    sair = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if sair in "Nn":
        break
for c in range(len(listaGeral)):
    if listaGeral[c] % 2 == 0:
        pares.append(listaGeral[c])
    else:
        impares.append(listaGeral[c])
print(f'Sua lista inicial foi {listaGeral}')
print(f'Após anlise e separar o npumeros pares dos ímpares tivemos\nLista Pares {pares}\nLista Ímpares {impares}')
