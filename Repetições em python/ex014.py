'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from os import system
x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
system('cls')
repete = True
while repete:
    print('\nO que quer fazer com {} e {} ?\n\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa'.format(x,y))
    aux = int(input('\nQual é a sua opção ?  '))
    if aux == 1:
        system('cls')
        print('\n{} + {} = {}'.format(x,y,x+y))
    elif aux == 2:
        system('cls')
        print('\n{} x {} = {}'.format(x,y,x*y))
    elif aux == 3:
        system('cls')
        print('\nO maior valor entre {} e {} é {}'.format(x,y,max(x,y)))
    elif aux == 4:
        system('cls')
        x = int(input('\nPrimeiro valor: '))
        y = int(input('Segundo valor: '))
    elif aux == 5:
        system('cls')
        repete = False
    else:
        system('cls')
        print('\nOpção inválida !')
print('\nVocê saiu do programa')