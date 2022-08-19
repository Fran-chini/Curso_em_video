'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

OBS: Números primos são Diviveis apenas por 1 e por ele mesmo, no intervalo do número ele não é divisível
'''

primo = int(input('Digite um número: '))
multiplo = 0 #Somador para armazenar os números divíveis pelo contador
for c in range(1, primo + 1): #Para C no intervalo de 2 até o valor digitado pelo usuário faça:
    if primo % c == 0: #Se o resto da divisão do número digitado pelo usuário for 0
        multiplo += 1 #Armazena 1 em multiplicador para identificar qual seu multiplicador.
if multiplo == 2:
    print('É Primo')
else:
    print('Não Primo')