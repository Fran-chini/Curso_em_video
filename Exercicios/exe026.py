#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

palavra = str(input('Digite uma frase: ')).strip()
palavra = palavra.lower() #Para evitar a sensibilidade do python, tratei a frase para ficar sempre em minuscula.
print('{} vezes aparece a letra A'.format(palavra.count('a'))) #Usei count() para contar a letra A que foi solicitado
print('A letra A aparece primeiro na posição {}'.format(palavra.find('a'))) #Find procura a palavra que se pede e traz a primeira posição que ele começa.
print('A letra A aparece por último na posição {}'.format(palavra.rfind('a'))) #rFind puxa á última posição da palavra pedida.
