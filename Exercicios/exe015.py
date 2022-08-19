#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60.00 dia e R$0.15 por Km rodado.
import time
print('-' * 80)
print('|{:^78}|'.format('CARROS ALUGADOS'))
print('-' * 80)
diaria = float(input('Qual valor do dia do carro alugado? R$'))
print('-' * 80)
kmrodado = float(input('Qual valor do Km rodado? R$'))
print('-' * 80)
dias = int(input('Por quantos dias deseja alugar o carro? '))
print('-' * 80)
km = float(input('Qual a média de Km irá rodar? '))
print('-' * 80)
print('|{:^78}|'.format('PROCESSANDO...'))
print('-' * 80)
time.sleep(2)
apagardia = diaria * dias
apagarkm = km * kmrodado
print('*' * 80)
print('|{:^78}|'.format('VALOR A PAGAR'))
print('*' * 80)
print('Alugando um carro por {} dias, com custo de R${:.2f} por dia, você pagará R${:.2f}'.format(dias, diaria, apagardia))
print('Calculando {:.2f} Km, sendo que cada Km custa R${:.2f}, pagará R${:.2f} '.format(km, kmrodado, apagarkm ))
print('Total a pagar pelo aluguél do carro R${:.2f}'.format(apagardia + apagarkm))
print('-' * 80)
print('|{:^78}|'.format('FIM DO PROCESSO'))
print('-' * 80)
