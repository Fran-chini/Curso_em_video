'''Cores no terminal - Aula Extra

Padrão ANSI -  Escape Sequence
Para adicionar a cor começamos com \033[ Estilo da fonte, texto, background m

Código de cores

Stile - Estilo
0 - Sem cor (None)
1 - Negrito (Bold)
4 - Underline (Sublinhado)
7 - Negativo (Inverte as cores)

Text - Cores de texto

30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Magento
36 - Ciano
37 - Cinza (Cor Padrão)

Background - Cor de fundo

40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Magento
46 - Ciano
47 - Cinza (Cor Padrão)

\033[0:33:44m #Estrutura para adicionar cor

exemplos

\033[0:30:41m #Cor do texto branca com fundo vermelho
\033[4:33:44m #Texto amarelo com sublinhado e fundo azul
\033[1:35:43m #Texto em magento com fundo amarelo
\033[30:42m #Texto em brando com fundo verde
\033[m #Volta as configurações para a cor padrão do terminal
\033[7:30m #Inverte as cores do texto


#---------------------------------------------------------------------------------

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))'''













