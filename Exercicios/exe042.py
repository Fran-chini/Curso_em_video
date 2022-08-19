'''Refaça o DESAFIO 35 dos triângulos , acrescentando o recurso de mostrar que tipo de triângulo
será formado.

 - EQUILÁTERO: todos os lados são iguais
 - ISÓSCELES: dois lados são iguais
 - ESCALENO: todos os lados diferentes'''

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 and lado1 == lado3:
        print('Com as medidas {} x {} x{} pode ser feito um triângulo Equilátero! '.format(lado1, lado2, lado3))
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Com as medidas {} x {} x {} pode ser feito um triângulo Isósceles!'.format(lado1, lado2, lado3))
    else:
        print('Com as medidas {} x {} x {} podemos fazer um triângulo Escaleno!'.format(lado1, lado2, lado3))
else:
    print('Com as medidas {} x {} x {} não podemos fazer um triângulo!'.format(lado1, lado2, lado3))