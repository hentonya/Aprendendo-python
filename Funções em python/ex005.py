# Faça um programa que tenha uma lista chamada números e duas funções chamadas 
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
# pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cont in range(0,5):
        lista.append(randint(0,10))
        sleep(0.5)
        print(lista[cont],end=' ',flush=True)
    print('Pronto!')
def somaPar(lista):
    acul = 0
    for cont in lista:
        if cont % 2 == 0:
            acul += cont
    print(f'Somando os valores pares de {lista}, temos {acul}')
    

números = list()
sorteia(números)
somaPar(números)