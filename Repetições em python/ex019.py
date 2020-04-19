'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a 
condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
repete = True
num = acumulador = contador = 0
while repete:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        repete = False
    else:
        acumulador += num
        contador += 1
print('Foram digitados {} números e a soma entre eles é {}'.format(contador,acumulador))
