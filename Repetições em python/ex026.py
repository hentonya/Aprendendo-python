"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao 
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas 
cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
cédulas = [ 50 , 20 , 10 , 1 ]
valor = int(input('Valor do saque ? R$ '))
quantidade = 0 
for c in range (0,4):
    quantidade = valor // cédulas[c]
    print(f'Total de {quantidade } cédulas de R$ {cédulas[c]}')
    valor = valor - quantidade * cédulas[c]
    if valor == 0:
        break
