'''
Crie um programa que leia uma frase qualquer e diga se elá é Palíndromo, desconsidrando os espaços

OBS: Palíndromo são frases que se lendo de trás para frente é a mesma coisa

Ex:

Apos a sopa
A sacada da casa
A torre da derrota
O lobo amo o bolo
Anotarama data da maratona
'''

palavra = str(input('Digite a frase: ')).strip().lower()
palavra = palavra.replace(' ', '')
invertido = palavra[::-1]

if palavra == invertido:
    print('A palavra é Palíndromo')
else:
    print('A palavra não é Palíndromo')
