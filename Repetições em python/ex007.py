#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
number = int(input('Digite um número inteiro: '))
aux = 0
for c in range (1, number + 1):
    if number % c == 0:
        aux+=1
        print('\033[31m{}\033[m'.format(c),end=' ')
    else:
        print(c,end=' ')
if aux == 2:
    print('\nO número {} é primo'.format(number))
else:
    print('\nO número {} foi divisível {} vezes, portanto não é primo'.format(number, aux))
