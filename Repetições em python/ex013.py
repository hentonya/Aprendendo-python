''' O computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer '''
from random import randint
from time import sleep
from os import system
aux = 1
print(20*'-=-'+'\nVou pensar em um número entre 0 e 10, tente advinhar !\n'+20*'-=-')
num1 = int(input('Em que número eu pensei ? '))
num2 = randint(0,10)
print('PROCESSANDO...')
sleep(1)
while num1 != num2:
    system('cls')
    num1 = int(input(('Número errado, tente novamente: ')))
    aux += 1
    print('PROCESSANDO...')
    sleep(1)
system('cls')
print('PARABÉNS! Você conseguiu me vencer depois de {} tentativas'.format(aux))