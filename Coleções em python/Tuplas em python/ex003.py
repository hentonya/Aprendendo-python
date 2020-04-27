"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois 
disso, mostre a listagem de números gerados e também indique o menor e o maior valor que 
estão na tupla.
"""
from random import sample
numbs = tuple(sample(range(1,11),5)) 
print(numbs)
print(f'O maior valor é {max(numbs)} e o menor é {min(numbs)}')
