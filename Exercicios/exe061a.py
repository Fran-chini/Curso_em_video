'''
Refaça o desafio 51, lendo o primeiro termo e a raão de uma PA, mostrando os 10 primeiros termos
da progressão usando While

"A fórmula do termo geral da progressão aritmética é a seguinte:

an = a1 + (n – 1) * r

'''
#------------Resposta GUanabara----------

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 1

while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    c += 1
print('FIM!')
