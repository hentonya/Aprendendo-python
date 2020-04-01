#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
num = radians(float(input('Digite o ângulo que você deseja: ')))
print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(sin(num),cos(num),tan(num)))
