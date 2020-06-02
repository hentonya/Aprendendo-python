# Faça um programa que tenha uma função chamada ficha(), que receba dois 
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa 
# deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha 
# sido informado corretamente.
def ficha(nome = '<desconhecido>', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome,gols)
