# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#Obs: Procurar bibliotecas que faça sorteio de String.

import random
nome = input('Digite o 1 nome para sortear: ')
nome2 = input('Digite o 2 nome para sortear: ')
nome3 = input('Digite o 3 nome para sortear: ')
nome4 = input('Digite o 4 nome para sortear: ')
lista = [nome, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de sorteio é:')
print(lista)

