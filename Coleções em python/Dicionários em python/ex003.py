# Crie um programa que leia nome, ano de nascimento e carteira de 
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso 
# a CTPS for diferente de ZERO, o dicionário receberá também o ano 
# de contratação e o salário. Calcule e acrescente, além da idade, 
# com quantos anos a pessoa vai se aposentar.
from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['ano de nascimento'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho (digite 0 se não possuir): '))
pessoa['idade'] = date.today().year - pessoa['ano de nascimento']
if pessoa['CTPS'] != 0:
    pessoa['ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['idade da aposentadoria'] = 35 - (date.today().year - pessoa['ano de contratação']) + pessoa['idade']
print('='*40)
for k, v in pessoa.items():
    print(f'-{k}: {v}')