'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
from os import system
from emoji import emojize
system('cls')
for c in range (10, -1, -1):
    print(c)
    sleep(1)
    system('cls')
print((emojize(':fireworks::tada::confetti_ball::boom::fireworks::tada::confetti_ball::boom:',use_aliases=True)))
