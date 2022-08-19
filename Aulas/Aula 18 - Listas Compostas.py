'''
list() = Lista mutável
append() = Comando que adiciona elementos no final da lista
lista = [['Pedro', 25], ['Maria', 19], ['João', 32]]
A lista composta é uma lista dentro da outra, cada um com seu prórpio indice, no exemplo acima o indeces são:
['Pedro', 25] = Posição 0 da lista mãe, Nome da posição 0 e idade na posição 1
['Maria', 19] = Posição 1 da lista mão, Nome na posição 0 e idade na posição 1

e assim sucessivamente para todos os elementos dentro da lista, cada lista tem seu próprio indice.

para acessar a listas dentro das lista ficaria:

lista = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(lista[0][0]) = O printe vai procurar a informa na lista mãe que está na posição 0 que é ['Pedro', 25] e dessa sublista irá escrever "Pedro" que está na posição 0
# >>> Pedro
print(lista[1][1])  = Segue o mesmo principio da explicação anterior, no indice 1 da lista mãe que é ['Maria', 19] irá exibir a posição 1 dessa sublista que é 19
# >>> 19
print(lista[1]) = Irá exibir a sublista na posição 1, que é ['Maria', 19]
# >>> ['Maria', 19]
'''

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # Faz uma cópia da lista teste, sem que faça alterações quando houver
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # Lista Composta
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
menorIdade = maiorIdade = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maiorIdade += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menorIdade += 1
print(f'Temos {maiorIdade} maiores de idade e {menorIdade} menores de idade.')'''
