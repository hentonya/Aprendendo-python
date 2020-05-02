""" 
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os 
valores únicos digitados, em ordem crescente. 
"""
numbers = list()
while True:
    num = int(input('Digite um número: '))
    if num not in numbers:
        numbers.append(num)
    else:
        print('Esse número já foi digitado, não irei armazená-lo')
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja adicionar mais números ? [S/N] ')).strip().lower()[0]
    if escolha == 'n':
        break
numbers.sort()
print(f'Números digitados em ordem crescente: {numbers}')
