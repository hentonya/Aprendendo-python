"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, 
mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numbers = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'\n{numbers}')
print(f'\nQuantidade de vezes que o número 9 apareceu: {numbers.count(9)}')
if 3 in numbers:
    print(f'O número 3 apareceu  primeiro na {numbers.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Números pares: ', end = '')
for c in numbers:
    if c % 2 == 0:
        print(c, end = '  ')
print('\n')
