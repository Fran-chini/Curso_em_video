#!/usr/bin/env python
# coding: utf-8

# ## Aula 19 - Dicionários
# 
# 
# Para declara um dicionário em Python: 
#     nome = dict() ou nome = {}
#     
# Ex:
#     dados = {'Nome':'Pedro', 'Idade':25}
# 
# Para exibir as informações de dentro dos Dicionários:
#     
#     print(dados['Nome']) = saída: Pedro
#     ou
#     print(dados['Idade'] = saída: 25
#     
# Para inserir um novo dado em uma lista:
#     dados['sexo'] = 'M'
#    
# Para deletar alguma informação do dicionário:
#     del dados['Idade']
# 
# 
# Novo dicionário armazenado dados de um filme:
# 
# filme = {'Nome':'Star Wars',
# 'Ano': 1977,
# 'Diretor':'George Lucas'
# }
# 
# Em dicionário cada informação alocada tem seu próprio nome, como :
# 
# Star Wars, 1977, George Lucas = Valores ou values()
# Nome, Ano, Diretor = Chaves ou keys()
# 
# ou seja, quando for necessário extrair essas informções ficaria o seguinte:
# 
# print(filme.values()) = Saída: Star Wars, 1977, George Lucas
# print(filme.keys()) = Saída: Nome, Ano, Diretor
# 
# Já para trazer todas as informações imguais as cadastradas dentro do dicionário:
# 
# print(filme.items()) = Saída: 'Nome':'Star Wars', 'Ano': 1977, 'Diretor':'George Lucas'
# 
# 
# Para usarmos for com dicionários por exemplo:
# 
# Significado: k = keys() | v = values()
# 
# logo:
# 
# for k, v in filme.items():
#     print(f'O {k} é {v}')
# 
# Saída: O titulo é Star Wars
# Saída: O ano é 1977
# Saída: O diretor é George Lucas
# 
# E assim o for irá percorrer todos os elementos dentro do dicionário.
# 
# Podemos adicionar os dicionários dentro de uma lista.
# 
# Ex:
# 
# locadora = [{'Titulo':'Star Wars', 'Ano':1977, 'Diretor':George Lucas'},{'Titulo':'Avengers', 'Ano':2012, 'Diretor':'Joss Whedon'},{'Titulo':'Matrix', 'Ano':1999, 'Diretor': 'Wachowski'}]
# 
# Sessa forma temos três dicionários dentro de uma lista e, para chamar essas informações ficaria o seguinte:
# 
#     print(locadora[0]['Ano']) = Saída: 1977
#     print(locadora[2]['Titulo'] = saída: Avengers
#     
# 

# In[4]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')


# In[5]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.keys())


# In[6]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.values())


# In[7]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.items())


# In[8]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)


# In[9]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k, v in pessoas.items():
    print(f'{k} = {v}')


# In[10]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')


# In[12]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')


# In[13]:


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')


# In[14]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(estado1)


# In[15]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(estado2)


# In[16]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)


# In[17]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])


# In[18]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1])


# In[19]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])


# In[20]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])


# In[21]:


brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP' }
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])


# In[25]:


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

    


# # Exercícios Aula 19

# Exercício 90:
# 
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# 
# 

# Exercício 91:
#     
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde asses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# 
# 
# 

# Exercicio 92:
# 
# Crie um programa que leia nome, data de nascimento(calcule a idade e armazene ao invés da data) e carteira de trabalho e cadastre-os (com idade) em um dicionário, se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# 
# 

# Exercício 93:
# 
#  Crie um programa que gerencie o aproveitamento de jogador de fatubol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final , tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o compeonato.
#  
#  

# Exercício 94:
# 
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. no final, mostre:
# 
# A) Quantas pessoas foram cadastrada.
# 
# B) A média de idade do grupo.
# 
# C) Uma lista com todas as mulheres.
# 
# D)Uma lista com todas as pessoas com idade acima da média.
# 
# 

# Exercício 95:
# 
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
