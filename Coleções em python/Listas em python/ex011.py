# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
# quantos  jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo 
# em uma lista composta.
from random import sample
from time import sleep
print( 30 * '-' )
print(f'{"MEGA SENA":^30}')
print( 30 * '-')
n = int(input('Quantos jogos deseja gerar ? '))
jogos = list()
print()
for c in range (n):
    jogos.append(sample(range(1,61), 6))
print(f'{" Gerando jogos ":-^30}')
for pos, cont in enumerate(jogos):
    sleep(1)
    print(f'Jogo {pos + 1}: {sorted(cont)}')
print(f'{" Boa sorte ":-^30}')