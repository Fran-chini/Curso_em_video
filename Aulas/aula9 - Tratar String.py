#Fatiamento de String
frase = 'Curso em video Python'
print(frase[9:21:2]) #estrutura desse fatiamento acontesse da seguinte forma 'Indice inicio : Indice Final : De quantas em quantas casas pula a leitura
print(frase[:5])#Dessa forma sem colocar indice inicial o Python vai começar do indice 0 até 5
print(frase[15:]) # Da mesma forma que a relação de cima o Python lê o indice inicial e vai até final
print(frase[9::3]) # Dessa forma ele tem indici inicial, vai até o final, pelando de 3 em 3

#Analisar uma String

print('A string contém {} caracteres'.format(len(frase))) #len() - Lê o comprimento dos caracteres
print('A String contém {} quantidades de letra O'.format(frase.count('o'))) # A função count irá contar quatos 'O' tem na string da 'frase'
print('Entre o indice 0 e 13 contém {} letra(s) O'.format(frase.count('o', 0, 13))) # Dessa forma a função count irá contar quantos 'o' tem na frase entre o indice 0 e 13, lembrando que o último indice não é considerado
print('A plavra começa na posição {}'.format(frase.find('deo'))) # Find significa encontrar algo. Nesta função o find retornará o inicio do indice que ele encontrou a palavra DEO.
print('Se o retorno der -1, significa que find não encontrou {}'.format(frase.find('Android'))) # Por não existir essa palavra dentro da string de frase, find irá retornar -1 como não encontrado
print('Curso' in frase) # Retorna True ou False de a palavra existir na String analisada.

# Transformação: Uma lista de string é imutável, não tem como mexer, mas usando métodos sim.

# Função .replace - Reposiciona a string

print(frase.replace('Python', 'Android')) # aqui o replace trocou a frase encontrada Python por Android, mesmo a string sendo imutável.

#Método .upper{} - Faz a String ser completamente em maiuscula

print(frase.upper()) # Deixa frase toda a string em Maiúscula
print(frase.lower()) # Deixa toda a string em minúscula
print(frase.capitalize()) # Deixa uma string inteira em minúscula e deixar somente a primeira letra maiúscula
print(frase.title()) # Vai deixar as primeiras letras de toda a string em maiúscula

frase = '   Aprenda Python  '

print(frase.strip()) # Remove todos os espaços desnecessários em uma string
print(frase.rstrip()) # Remove os espaços de uma string somente do lado direito
print(frase.lstrip()) # Remove os espaços de uma string somente do lado esquerdo

#Junção de String

frase = 'Curso em Video Python'
# O split faz divisão da string onde tiver espaços e criar uma nova indexação e cada nova palavra terá uma nova lista.
print(frase.split()) # ESTUDAR MAIS SOBRE
nfrase = frase.split() # Adicionei uma nova string para receber a frase splitada para usar em join como exemplo
print('-'.join(nfrase)) # Join usa a nova indexaçã de split unir as pelavras com o caractere que definimos antes de join '-'
print(nfrase[2][3]) # Nessa forma conseguimos pegar de acordo com a frse splitada um indice e dentro dele buscar uma letro ou informação.

#PARA DAR PRINT EM UM TEXTO SEM PRECISAR SER LINHA LINHA

print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento 
de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), 
strip(), junção com join().""")





