'''
Crie um programa que mostre na tela todos os números pares que estão no
intervalo entre 1 e 50

OBS: Usar o Iterador +2 no looping FOR
'''

for c in range(1, 52): #Para C dentro do intervalo de 1 a 50 conte.
    if c % 2 == 0: # Se o resto da divisão de C por 2 for igual a 0, então o número é e ele pode ser exibido
        print(c, end=' ') #exibição do número par, "end faz com que ao terminar o porint não vá para a linha de baixo.
print('Fim de contagem!')