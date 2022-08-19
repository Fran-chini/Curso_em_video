#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da Cidade: ').strip()
cidade = cidade.capitalize()# Para evitar todas as formas de escrita santos, formatei  primeiro bloco para que sempre fique formatado a palavra padrão Ex: SanTos == Santos
cidade1 = cidade.split() #Esse tratamento irá dividir a palavra digitada em blocos
cidade1 = cidade1[0] #Armazenei na variavel o bloco 0, o que resulta na primeira palavra digitada
if cidade1 == 'Santo': #Aqui eu a variável já formatada com a palavra Santos, dessa forma nunca irá dar problemas.
   print('A cidade {} começa com Santos!'.format(cidade))
else:
   print('A cidade {} não começa com Santos!'.format(cidade))
