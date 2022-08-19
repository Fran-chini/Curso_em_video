'''
Refazer o exercicio da tabuada usando um número que o usuário irá digitar e mostrar a tabuada desse valor
'''

num = int(input('Digite o número para a tabuada: '))
print('Tabuada do {}'.format(num))
for c in range(1,11):
    print('{} x {:>2} = {:>2}'.format(num, c, num * c))