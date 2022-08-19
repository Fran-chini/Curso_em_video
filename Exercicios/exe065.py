'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR
valores lidos. O programa deve perguntar se o usuário quer ou não CONTINUAR a digitar valores.

'''
resp = 's'
count = maior = menor = soma = média = 0
while resp == 's':
    count += 1
    n = int(input('Digite um número: '))
    soma += n
    if count == 1:
        maior = menor = n
    if n >= maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Deseja continuar?[S/N] ')).strip().lower()
média = soma / count
print('A média entre os números digitados foi {:.2f}.\nO maior número foi {} e o menor foi {}.'.format(média, maior, menor))