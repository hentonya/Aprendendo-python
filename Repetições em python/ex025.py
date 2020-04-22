"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar 
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
total = cont2 = cont1 = preço_barato = 0
barato = ''
while True:
    produto = str(input('\nNome do produto: ')).strip().upper()
    preço = float(input('Preço do produto: R$ '))
    total += preço
    if preço > 1000:
        cont2 += 1 
    if cont1 == 0 or preço < preço_barato:
        barato = produto
        preço_barato = preço
    cont1 += 1 
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if escolha == 'n':
        break
print('\n'+20*'='+' Fim do programa ' + 20*'='+'\n')
print(f'Total gasto na compra: R$ {total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000: {cont2}')
print(f'O produto mais barato é {barato} que custa {preço_barato}')
