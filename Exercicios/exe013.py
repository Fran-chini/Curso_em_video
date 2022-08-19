#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual seu salário R$'))
aum = sal * (15/100)
nsal = sal + aum
print('Salario atual R${:.2f}\nAumento de 15% R${:.2f}\nSeu novo salário será R${:.2f}'.format(sal, aum, nsal))
