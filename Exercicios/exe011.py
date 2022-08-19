#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

alt = float(input('Qual a altura da parede(Métros): '))
larg = float(input('Qual a largura da parede(Métros): '))
area = alt * larg
tinta = area / 2
print('Sua parede tem {:.2f}M²\nVocê precisará de {:.2f} Litros de tinta'.format(area, tinta))
