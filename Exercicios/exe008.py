#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print('-'*50)
print('|{:^48}|'.format('OPÇÕES DE MEDIDAS'))
print('-'*50)
print('Escolha uma opção para conversão')
print('(1) Milímetro\n(2) Centímetro\n(3) Decímetro\n(4) Decâmetro\n(5) Hectômetro\n(6) Quilômetro')
opcao = int(input(''))
if opcao == 1:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA MILÍMETROS'))
    print('-'*50)
    medida = float(input('Digite o valor para conversão: '))
    mili = medida * 10 * 10 * 10
    print('{: .2f} métros equivalem á {: .2f} milímetros'.format(medida, mili))
    print('-'*50)
    print('|{:^48}|'.format('Conversão Concluída'))
    print('-' * 50)
if opcao == 2:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA CENTÍMETROS'))
    print('-'*50)
    medida = float(input('Digite o valor para conversão: '))
    cent = medida * 10 * 10
    print('{:.2f} métros equivalem a {:.2f} Centímetros'.format(medida, cent))
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO CONCLUÍDA'))
    print('-'*50)
if opcao == 3:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA DECÍMETROS'))
    print('-'*50)
    medida = float(input('Digite o valor para conversão: '))
    dec = medida * 10
    print('{:.2f} métros equivalem a {:.2f} Decímetros'.format(medida, dec))
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO CONCLUÍDA'))
    print('-'*50)
if opcao == 4:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA DECÂMETRO'))
    print('-'*50)
    medida = float(input('Digite o valor para conversão: '))
    dec = medida / 10
    print('{:.2f} métros equivalem á {:.2f} decâmetros'.format(medida, dec))
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO CONCLUIDA'))
    print('-'*50)
if opcao == 5:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA HECTÔMETRO'))
    print('-'*50)
    medida = float(input('Digite o valor para conversão: '))
    hec = medida / 10 / 10
    print('{:.2f} métros equivalem á {:.2f} hectômetros'.format(medida, hec))
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO CONCLUÍDA'))
    print('-'*50)
if opcao == 6:
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO DE MÉTROS PARA QUILÔMETROS'))
    print('-'*50)
    medida = float(input('Digite um valor para conversão: '))
    qui = medida / 10 / 10 / 10
    print('{:.2f} métros equivalem á {:.2f} quilômetros'.format(medida, qui))
    print('-'*50)
    print('|{:^48}|'.format('CONVERSÃO CONCLUÍDA'))
    print('-'*50)
