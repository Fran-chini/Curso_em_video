#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido
# Obs: Biblioteca Random tem função de sortear

import random
nome = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
lista = [nome, nome2, nome3]
print('O aluno sorteado para apagar o quadro é {}. '.format(random.choice(lista)))
