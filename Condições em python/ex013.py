''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a 
idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER '''
from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <=9:
    print('A categoria de alguém com {} anos é MIRIM'.format(idade))
elif idade <= 14:
    print('A categoria de alguém com {} anos é INFANTIL'.format(idade))
elif idade <= 19:
    print('A categoria de alguém com {} anos é JÚNIOR'.format(idade))
elif idade <= 25:
    print('A categoria de alguém com {} anos é SÊNIOR'.format(idade))
else:
    print('A categoria de alguém com {} anos é MASTER'.format(idade))
