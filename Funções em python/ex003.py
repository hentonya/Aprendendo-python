# Faça um programa que tenha uma função chamada contador(), que receba três 
# parâmetros: início, fim e passo. Seu programa tem que realizar três contagens 
# através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contador(início, fim, passo):   
    if passo == 0:
        passo = 1
    if fim < início and passo > 0:
        passo *= -1
        print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
        fim -= 1
    elif fim > início and passo < 0:
        passo *= -1
        print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
        fim += 1
    elif passo < 0:
        print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
        fim -= 1
    else:
        print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
        fim += 1
    for num in range(início,fim,passo):
        sleep(0.5)
        print(num,end=' ',flush = True)
    print('FIM!')


print(50*'=')
contador(1,10,1)
print(50*'=')
contador(10,0,2)
print(50*'=')
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))
print(50*'=')
