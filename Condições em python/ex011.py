'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda 
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu 
programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade == 18:
    print('Quem nasceu em {} tem {} anos em {} '.format(ano,idade,date.today().year))
    print('\033[31mVOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE !\033[m')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {} '.format(ano,idade,date.today().year))
    print('Você já deveria ter se alistado há {} {}'.format(idade - 18, 'anos' if idade - 18 > 1 else 'ano'))
    print('Seu alistamento foi em {}'.format(ano + 18))
else:
    print('Quem nasceu em {} tem {} {} em {} '.format(ano,idade,'anos' if idade >  1 else 'ano',date.today().year))
    print('Ainda {} {} {} para o alistamento'.format('faltam' if 18 - idade > 1 else 'falta',18 - idade, 'anos' if 18 - idade > 1 else 'ano'))
    print('Seu alistamento será em {}'.format(ano + 18))
