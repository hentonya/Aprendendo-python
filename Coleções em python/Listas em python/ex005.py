"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas 
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao 
final, mostre o conteúdo das três listas geradas.
"""
números = list()
pares = list()
ímpares = list()
while True:
    números.append(int(input('Digite um número: ')))
    if números[-1] % 2 == 0:
        pares.append(números[-1])
    else:
        ímpares.append(números[-1])
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar ? [Sim/Não] ')).upper().strip()[0]
    if escolha == 'N':
        break
print( 30 * '-=')
print(f'A lista completa é {números}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')

