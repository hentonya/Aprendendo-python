# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias 
# consecutivas que ele conquistou no final do jogo. 
from random import randint
vitorias = 0 
while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Par ou ímpar ? [P/I] ')).strip().lower()[0]
    if escolha == 'í':
        escolha = 'i'
    computador = randint(1,10)
    print(f'Você jogou {jogador} e o computador jogou {computador}\nO total é {jogador + computador}')
    if (jogador + computador) % 2 == 0:
        resultado = 'p'
    else:
        resultado = 'i'
    if resultado == escolha:
        vitorias += 1 
        print('\nPARABÉNS !, você venceu\nVamos jogar novamente')
    else:
        break
print(f'GAME OVER\nVocê ganhou {vitorias} vezes')
