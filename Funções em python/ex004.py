# Faça um programa que tenha uma função chamada maior(), que receba vários 
# parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e 
# dizer qual deles é o maior.
from time import sleep
def maior(*n):
    print(50*'=')
    print('Analisando os valores passados...')
    sleep(2)
    if len(n) > 0:
        for c in n:
            sleep(0.5)
            print(c, end=' ',flush=True)
    else:
        print('0',end='')
    sleep(1.5)
    print(f'\nForam informados {len(n)} valores ao todo')
    sleep(1.5)
    print(f'O maior valor informado foi {max(n) if len(n) > 0 else 0 }')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()