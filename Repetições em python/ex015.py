#Faça um programa que leia um número qualquer e mostre o seu fatorial
num = int(input('Digite um número para calcular seu fatorial: '))
result = 1
print('{}! = '.format(num), end= '')
while num > 0:
    result *= num
    if num > 1:
        print('{} x'.format(num), end = ' ')
    else:
        print('{} ='.format(num), end = ' ')
    num -= 1
print(result)
