#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
massas = [0,0,0,0,0]
for c in range (0,5):
    massas[c] = float(input('Peso da {}ª pessoa: '.format(c+1)))
print('O maior peso lido foi {} kg\nO menor peso lido foi {} kg'.format(max(massas), min(massas)))
