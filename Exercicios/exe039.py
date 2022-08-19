#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
sexo = str(input('Qual seu Sexo? [M]/[F]')).strip().lower()
if sexo == "m":
    ano_nascimento = int(input('Qual ano de nascimento: '))
    ano_atual = date.today().year
    idade = abs(float(ano_atual) - ano_nascimento)
    if idade == 18:
        print('Está na hora de se alistar!')
    elif idade > 18:
        print('Passou a hora de se alistar!\nVocê deveria ter se alistaso no ano de {}'.format(ano_nascimento+18))
    else:
        print('Sua hora de se alistar vai chegar!\nFaltam {:.0f} ano(s) para seu alistamento!\nO ano para o seu alistamento será {}'.format(abs(idade - 18), ano_nascimento+18))
else:
    print('O alistamento é obrigatório apenas para o sexo Masculino!')