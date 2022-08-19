'''
Estrutura de repetição!
Iteração!

For (Para Faça)
While (Enquanto Faça)

Laço de repetição ou Iteração (Laço com variável de controle)

for count in range(parâmetro): - Range siguinifica intervalo
'''


#####Aula prática#####

'''for c in range(1, 6):
    print('Oi')
print('FIM')'''

'''for c in range(6, 0, -1): # O -1 é a iteração do for, fazendo com que o contador retire 1 número para fazer a contagem regressiva.
    print(c)
print('FIM')'''
s = 0
for c in range(0, 3): # Pergunta um número de 0 até 2
    n = int(input('Digite um número: '))
    s += n #Soma os valores digitados
print('Total {}'.format(s))
