'''
Listas = [] - Listas são mutáveis ou seja, termos como alterar valores dentro delas.

.append() - Adiciona um elemento no fim da lista
.insert() - Podemos adicionar um elemento em qualquer lugar da lista .inset(posição, 'COloque esse elemento')
del - Usado para excluir um elemento da lista
.pop(posição) - Usado para eliminar lo ultimo elemento da lista, mas passando a posição também da certo por exemplo lanche.pop(3)
.remove(posição) - Podemos remover um elemento da lista passando como parametro o nome por exemplo posição 0 = 'Pizza' logo lanche.remove('Pizza')
.sort() - Coloca os elementos ordenados em forma crescente.
.sort(reverse=True) - Passa os parametros da lista em ordem decrescente
.len() - Conta quantos elementos tem dentro de uma lista, tupla, dicionario

if 'Pizza' in lanche:
    lanche.remove('Pizza')

Criar lista com Range():

valores = list(range(4, 11) -> Saida: [4, 5, 6, 7, 8, 9, 10]

'''

#PRÁTICA

'''num = [2, 5, 9, 1] #Lista de números
print(num) #Exibi na tela a lista original
num[2] = 3 #Inseri na posição 2 o número 3, logo o 9 passa a ser 3
print(num) #Exibi a nova lista alterando o 9 para 3
num.append(7) #Adicionando o npumero 7 ao final da lista, mesmo que não haja espaço para tal.
print(num) #Exibi a nota lista com o número 7 incrementado.
num.sort() #Coloquei a lista em ordem crescente
print(num) #Exibi na tela a lista crescente
num.sort(reverse=True) #Coloquei a lista em ordem decrescente ou seja do maior para o menor.
print(num) #Exibi a nova lista em ordem decrescente
print(f'Aqui estou exibindo a quantidade de elementos dentro da lista {num} = {len(num)}')
num.insert(2, 2) #Estou inserindo na posição 2 da lista o número 2
print(num) #Exibi a lista com o número 2 inserido na posição 2
num.remove(2) #Remove busca o primeiro parametro 2 e o remove da lista deixando o último 2 para trás, para retirar todos devemos usar um laço de repetição
print(num) #Exibindo a lista sem o primeiro número dois.
if 4 in num: # Se caso houve o número 4 dentro da lista num ele irá remover
    num.remove(4) #Se for verdadeiro o npumero 4 será removido.
else:
    print('Não foi encontrado o número 4 na lista!') # Se for falso essa mensagem irá aparecer para o usuário
if 5 in num: # Se caso houve o número 5(O que tem) dentro da lista num ele irá remover
    num.remove(5) #Se for verdadeiro o npumero 4 será removido.
else:
    print('Não foi encontrado o número 4 na lista!') # Se for falso essa mensagem irá aparecer para o usuário
print(num) #Exibi a nova lista com o número 5 removido'''

#Outra forma de criar listas

'''valores = [] #Criei uma lista vazia
#valores.append(5) #Append adiciona dentro da lista 'VALORES' o número no seu parametro (5)
#valores.append(9) #Append adiciona dentro da lista 'VALORES' o número no seu parametro (9)
#valores.append(4) #Append adiciona dentro da lista 'VALORES' o npumero no seu parametro (4)

for cont in range(0, 5): #Para contador na posição inicial 0 faça o looping até 5.
    valores.append(int(input(f'Digite o {cont+1}º valor: '))) #Para ser mais dinâmico, em uma estrutura for podemos pedir qualuqer quantidade de valores a ser digitado

for c, v in enumerate(valores): # Para C e V (São contadores) na posição do enumerate(Função que passa a posição dos elementos na lista) faça a seguir:
    print(f'Na posição {c} encontrei o valor {v}!') #O For vai procurar dentro da lista na posição passada em C e V o valor que contem por exemplo: C = 0, na posição 0 da lista temos 5
print('Cheguei ao final da lista.')'''


#Peculiaridade em Python

a = [2, 3, 4, 7] #Criamos uma lista normal
b = a #Adicionamos a lista em A em B, porém o python faz uma ligação entre as listas, ou seja se eu alterar a lista B tambén altera a lista A.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

b[2] = 8 #Se B na posição 2 troca para o numero 8, como há aquela ligação o python troca nas duas listas.
print(f'Lista A: {a}')
print(f'Nova lista B: {b}')

#para fazer uma cópia da lista e armazenar e outra podemos usar o métodos de fatiamento.
b = a[:] #Lista B recebe lista todos os parametros da lista A, fazendo assim uma cópia
print(f'Cópia da lista A armazenada na Lista B: {b}')
b[2] = 10 #Agora fazendo a alteração colocando o número 10 na posição da lista B, isso não mudará a lista.

print(f'Lista A: {a}')
print(f'Lista B alterada: {b}')

