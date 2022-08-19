#Faça um programa que leia do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento
# da hipotenusa.
from math import hypot
catop = float(input('Qual o valor do Cateto Oposto: '))
catad = float(input('Qual o valor do Cateto Adjacente: '))
print('O tamanho da Hipotenusa equivale há {:.2f}.'.format(hypot(catop, catad)))
