# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário 
# em Python. No final, coloque esse dicionário em ordem, sabendo 
# que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogadores = dict()
for c in range (1,5):
    jogadores[f'Jogador {c}'] = randint(1,6)
print(40*'=')
print(f'{"VALORES SORTEADOS":^40}')
print(40*'=')
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print(40*'=')
print(f'{"RANKING DOS JOGADORES":^40}')
print(40*'=')
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse=True)
for i, c in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar: {c[0]} com {c[1]}')
print()