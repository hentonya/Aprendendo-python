"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense
"""
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',          
        'Internacional', 'Corinthians', 'Fortaleza EC', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
        'Chapecoense', 'Avaí')
print(20 * '=' + ' CAMPEONATO BRASILEIRO DE FUTEBOL ' + 20 * '=')
for posição, time in enumerate(times):
    print(f'{posição + 1:2}º {time}')
print(f'\n>>> OS 5 PRIMEIROS TIMES:\n')
for posição, time in enumerate(times[0:5]):
    print(f'{posição + 1}º {time}')
print(f'\n>>> OS ÚLTIMOS 4 COLOCADOS:\n')
for posição, time in enumerate(times[16:]):
    print(f'{posição + 17}º {time}')
print('\n>>> TIMES EM ORDEM ALFABÉTICA:\n')
for  time in sorted(times):
    print(f'{time}')
print(f'\n>>> O CHAPECOENSE ESTÁ NA {times.index("Chapecoense") + 1}º POSIÇÃO\n')
