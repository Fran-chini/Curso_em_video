#Conversor de Temperatura
#Celcius x Fahrenheit
#Celcius x Kelvin
#Fahrenheit x Celcius
#Fahrenheit x Kelvin
#Kelvin x Celcius
#Kelvin x Fahrenheit
import time
print('-' * 50)
print('|{:^48}|'.format('CONVERSOR DE TEMPERATURA'))
print('-' * 50)
print('(1) Graus Celcius x Graus Fahrenheit\n(2) Graus Celsius x Graus Kelvin\n(3) Graus Fahrenheit x Graus Celcius\n(4) Graus Fahrenheit x Graus Kelvin\n(5) Graus Kelvin x Graus Fahrenheit\n(6) Graus Kelvin x Graus Celcius')
opcao = int(input('Escolha uma opção acima: '))
print('-' * 50)
print('|{:^48}|'.format('PROCESSANDO...'))
print('-' * 50)
time.sleep(2.0)
if opcao == 1:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS CELSIUS X GRAUS FAHRENHEIT'))
    print('-' * 50)
    celsius = float(input('Quantos ºC deseja converter? '))
    res = (celsius * 9 / 5) + 32
    print('Convertendo {:.2f}ºC terá {:.2f}ºF'.format(celsius, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)
if opcao == 2:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS CELSIUS X GRAUS KELVIN'))
    print('-' * 50)
    kelvin = float(input('Quantos ºC deseja converter? '))
    res = kelvin + 273.15
    print('Convertendo {:.2f}ºC terá {:.2f}ºK'.format(kelvin, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)
if opcao == 3:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS FAHRENHEIT X GRAUS CELSIUS'))
    print('-' * 50)
    fah = float(input('Quantos ºF deseja converter? '))
    res = (fah - 32) * 5 / 9
    print('Convertendo {:.2f}ºF terá {:.2f}ºC'.format(fah, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)
if opcao == 4:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS FAHRENHEIT X GRAUS KELVIN'))
    print('-' * 50)
    fah = float(input('Quantos ºF deseja converter? '))
    res = (fah - 32) * 5 / 9 + 273.15
    print('Convertendo {:.2f}ºF terá {:.2f}ºK'.format(fah, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)
if opcao == 5:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS KELVIN X GRAUS FAHRENHEIT'))
    print('-' * 50)
    kel = float(input('Quantos ºK deseja converter? '))
    res = (kel - 273.15) * 9 / 5 + 32
    print('Convertendo {:.2f}ºK terá {:.2f}ºF'.format(kel, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)
if opcao == 6:
    print('-' * 50)
    print('|{:^48}|'.format('GRAUS KELVIN X GRAUS CELSIUS'))
    print('-' * 50)
    kel = float(input('Quantos ºK deseja converter? '))
    res = kel - 273.15
    print('Convertendo {:.2f}ºK terá {:.2f}ºC'.format(kel, res))
    print('-' * 50)
    print('|{:^48}|'.format('FIM DE PROCESSAMENTO'))
    print('-' * 50)