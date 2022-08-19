'''
Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500

OBS: Usar iterador +3 no looping de FOR
Precisa saber se ele é divisível por 3 ou seja usar %(Resto da divisão por três)

'''
soma = 0
guarda = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            guarda += 1
            soma += c
print('A soma dos {} números ímpares e multiplos de 3 é {}'.format(guarda, soma))
print('Fim de operação!')
