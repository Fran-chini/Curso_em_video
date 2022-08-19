# Faça um programa que leia 3 números e mostre qual é o MAIOR e qual é o MENOR
# num > num2
# num > num3
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
#verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado pe {}'.format(menor))












