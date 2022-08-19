# ESTRUTURAS CONDICIONAIS SIMPLES E COMPOSTAS (AULA 09)
#if else : Condição estrutural simples
#Aula Teórica
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')

#Aula Prática

nome = str(input('Qual seu nome? ')).strip()
if nome == 'William':
    print('Qua nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média é ruim! Estude mais!')
print('-' * 5,'FIM', '-' * 5)
