'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário,
escolher qual será a base de conversão.

1 - para Binário
2 - para Octal
3 - para Hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O {} convertido para BINÁRIO equivale a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O {} convertido para OCTAL equivale a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O {} convertido para Hexadecimal equivale a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida!')


