'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostralo por extenso.

'''
#Lista de tuplas com números por extenso.
listaNumeros = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
                'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = 21
    while num > 20:
        num = int(input('Digite um números entre 0 e vinte, para vê-lo escrito por extenso: '))
    print(f'Você digitou o número {listaNumeros[num]}')
    sair = str(input('Deseja parar?[S/N]')).strip().upper()[0]
    if sair == 'S':
        break
print('Fim algoritmo!')
