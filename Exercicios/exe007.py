#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
mat = str(input('Qual é a matéria escolar ?'))
print('-'*50)
print('|{:^48}|'.format(mat))
print('-'*50)
nota = float(input('Qual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))
media = (nota + nota2)/2
print('A média para a matéria de {} é {: .2f}'.format(mat, media))
if media < 5:
    print('-' * 50)
    print('|{:^48}|'.format('Aluno Reprovado!'))
    print('-' * 50)
if media >= 5:
    print('-' * 50)
    print('|{:^48}|'.format('Aluno Aprovado!'))
    print('-' * 50)