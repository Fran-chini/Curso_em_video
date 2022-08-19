# Desenvolve um programa que leia o comprimento de três retas e diga ao usúario se eles podem ou não
# formar um triângulo
#Basta fazer a soma entre os dois lados menores. Se a soma entre eles for maior que o terceiro lado, então,
# a soma entre qualquer um deles e o terceiro lado (que é o maior) terá o mesmo resultado.

lado1 = float(input('Digite o valor da 1 reta: '))
lado2 = float(input('Digite o valor da 2 reta: '))
lado3 = float(input('Digite o valor da 3 reta: '))
#encontrando lado maior

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Com as retas {} x {} x {} conseguimos fazer um triângulo!'.format(lado1, lado2, lado3))
else:
    print('Não é possivel fazer um triângulo com os valores {} x {} x {}.'.format(lado1, lado2, lado3))



