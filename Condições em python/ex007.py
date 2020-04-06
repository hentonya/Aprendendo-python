#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o comprimento 01: '))
b = float(input('Digite o comprimento 02: '))
c = float(input('Digite o comprimento 03: '))
if a < (b+c) and a > abs(b-c) and  b < (a+c) and b > abs(a-c) and  c < (a+b) and c > abs(b-a):
    print('Essas três retas PODEM formar um triângulo !')
else:
    print('Essas três retas NÃO PODEM formar um triângulo !')
