#Crie um programa que faça o computador jogar Jokenpô com você.
from emoji import emojize
from time import sleep
from random import randint
from os import system 
system('cls')
print('{:=^40}'.format(' JOKENPÔ '))
lista = ['PEDRA','PAPEL','TESOURA']
escolha1 = int(input((emojize('\nSuas opções:\n\n[ 0 ] PEDRA :fist:\n[ 1 ] PAPEL :hand:\n[ 2 ] TESOURA :v:\n\nQual é a sua jogada ? ', use_aliases=True))))
escolha2 = randint(0,2)
system('cls')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(0.5)
system('cls')
print(40*'='+'\nO computador jogou \033[31m{}\033[m\nVocê jogou \033[31m{}\033[m\n'.format(lista[escolha2],lista[escolha1])+40*'=' +'\n')
if escolha1 == escolha2:
    print('\033[31mEMPATE\033[m\n')
elif escolha1 == 0 and escolha2 == 1:
    print('\033[31mDERROTA\033[m\n')
elif escolha1 == 1 and escolha2 == 0:
    print('\033[31mVITÓRIA\033[m\n')
elif escolha1 == 0 and escolha2 == 2:
    print('\033[31mVITÓRIA\033[m\n')
elif escolha1 == 2 and escolha2 == 0:
    print('\033[31mDERROTA\033[m\n')
elif escolha1 == 1 and escolha2 == 2:
    print('\033[31mDERROTA\033[m\n')
elif escolha1 == 2 and escolha2 == 1:
    print('\033[31mVITÓRIA\033[m\n')
