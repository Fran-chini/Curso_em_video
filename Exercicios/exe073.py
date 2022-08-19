'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabel.
C) Uma lista com os times em ordem alfabética.
D) Em que posição está o time do Corinthians

'''

timesBrasileirao = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Santos',
                    'Flamengo', 'Fluminense', 'Botafogo', 'São Paulo', 'Bragentino', 'Avaí', 'Atlético-GO',
                    'Ceará SC', 'Coritiba', 'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')
print(f'Os cinos primeiros no brasileirão 2022 está {timesBrasileirao[:5]}')
print(f'Os quatros último colocados são {timesBrasileirao[-4:]}')
print(f'Lista em ordém alfabética: {sorted(timesBrasileirao)}')
print(f'Coritihinas está na {timesBrasileirao.index("Corinthians")+1}ª posição do Brasileirão 2022')


