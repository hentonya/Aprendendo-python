#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range (1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu ? '.format(c)))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Tivemos {} {} de idade\nJá menores de idade, tivemos {} {}'.format(maior,'pessoa maior' if maior == 1 else 'pessoas maiores', menor,'pessoa' if menor == 1 else 'pessoas'))
