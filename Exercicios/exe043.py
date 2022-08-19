'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

altura = float(input('Qual a sua altura: '))
peso = float(input('Qual seu peso: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Baixo do Peso!')
if 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Peso Ideal!')
if 25 < imc <= 30:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Sobrepeso!')
if 30 < imc <= 40:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Obesidade!')
if imc > 40:
    print('Seu IMC é {:.2f}'.format(imc))
    print('Obesidade Morbida!')