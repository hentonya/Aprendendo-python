# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, 
# mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list() # Lista utilizada para auxiliar na obtenção dos dados
pesos = list()
while True:
    dados.append(str(input('Nome da pessoa: ')).strip().capitalize())
    dados.append(float(input(f'Peso de {dados[0]}: ')))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    dados.clear()
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja adiconar mais pessoas ? [Sim/Não] ')).strip().lower()[0]
    if escolha == 'n':
        break
print(40 *'-=')
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi de {max(pesos)} KG. Peso de ', end = ' ')
for elemento in pessoas:
    if elemento[1] == max(pesos):
        print(f'[{elemento[0]}]', end = ' ')
print()
print(f'O menor peso foi de {min(pesos)} KG. Peso de', end = ' ')
for elemento in pessoas:
    if elemento[1] == min(pesos):
        print(f'[{elemento[0]}]', end = ' ')
 