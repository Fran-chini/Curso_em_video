'''
Crie uma programa com uam tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''

palavras = ('Subway', 'Comida', 'Frango', 'Cachorro', 'Computador', 'Microfone', 'Tela', 'Gato', 'Arroz', 'Anticonstitucionalissimamente', 'Mercado')
'''for c in range(0, len(palavras)):
    print(f'A palavra {palavras[c]} contém a vogais: ', end=' ')
    if 'a' in palavras[c]:
        print('a', end=' ')
    if 'e' in palavras[c]:
        print('e', end=' ')
    if 'i' in palavras[c]:
        print('i', end=' ')
    if 'o' in palavras[c]:
        print('o', end=' ')
    if 'u' in palavras[c]:
        print('u', end=' ')
    print(' ')
print('Fim de execução!')'''

#GUANABARA
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
