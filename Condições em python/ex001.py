#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
#escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print(20*'-=-'+'\nVou pensar em um número entre 0 e 5, tente advinhar !\n'+20*'-=-')
num1 = int(input('Em que número eu pensei ? '))
num2 = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if num1 == num2:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(num2,num1))
