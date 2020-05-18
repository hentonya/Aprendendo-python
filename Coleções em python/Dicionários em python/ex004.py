# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O 
# programa  vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler 
# a quantidade  de gols feitos em cada partida. No final, tudo isso será guardado 
# em um dicionário, incluindo o total de gols feitos durante o campeonato
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: ')).strip()
jogador['gols'] = list()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for c in range (0,jogador['partidas']):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c+1} ? ')))
jogador['total de gols'] = sum(jogador['gols'])
print(50*'=')
print(jogador)
print(50*'=')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}') 
print(50*'=')
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'     => Na partida {k+1}, fez {v} gols')
print(f'Foi um total de {jogador["total de gols"]} gols')