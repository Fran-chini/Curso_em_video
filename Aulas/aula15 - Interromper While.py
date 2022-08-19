'''
Na estrutura While, temos um termo que podemos parar o looping, que é Break.

f string está substituindo .format()'''
saida = 'FIM!'
while True:
    n = int(input('Digite número: '))
    if n == 999:
        break
print(f'{saida}')#Tratamento com f string, o que substituirá o .format mais a frente.