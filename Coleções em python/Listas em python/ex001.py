"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o 
maior e o menor valor digitado e as suas respectivas posições na lista. 
"""
num = list()
pos_max = list()
pos_min = list()
for cont in range (0,5):
    num.append(int(input(f'Digite um número para a posição {cont}: ')))
for posição, valor in enumerate(num):
    if valor == max(num):
        pos_max.append(posição)
    if valor == min(num):
        pos_min.append(posição)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições: {pos_max}')
print(f'O menor valor digitado foi {min(num)} nas posições: {pos_min}')
                                           