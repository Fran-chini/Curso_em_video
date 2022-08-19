#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangênte desse ângulo.
#Existe bibliotecas que tem soluções ágeis.
import math

angulo = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor de Seno é {:.2f}'.format(sen))
print('O valor de Cosseno é {:.2f}'.format(cos))
print('O valor de Tangênte é {:.2f}'.format(tan))
