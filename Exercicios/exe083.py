'''
Crie um programa que leia uma expressão qualquer que use parenteses. Seu aplicativo
deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

'''

lista = []
expressao = str(input('Digite a expressão: ')).strip()
aberto = fechado = 0
lista = [expressao[i:i+1] for i in range(0, len(expressao))]
aberto = lista.count('(')
fechado = lista.count(')')
if aberto == fechado and aberto != 0 and fechado != 0:
  print(f'A expressão {expressao} está correta!')
else:
  print(f'Verifique sua expressão! Algo deu errado!')

