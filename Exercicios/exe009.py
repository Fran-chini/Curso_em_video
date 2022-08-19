#Faça um prgrama que leia um número inteiro qualquer e mostre na tela a sua tabuada.
tab = int(input('Digite um valor para ver a Tabuada: '))
i = 1
while i <= 10:
    r = tab * i
    print('{} x {:2} = {:2}'.format(tab, i, r))
    if i == 10:
        break
    i += 1
