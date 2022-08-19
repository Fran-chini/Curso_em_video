# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calculem um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite seu salário R$'))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print('Seu novo salário com 10% de aumento será R${:.2f}'.format(salario))

else:
    salario = salario + (salario * 15 / 100)
    print('Seu novo salario com 15% de aumento R${:.2f}'.format(salario))
