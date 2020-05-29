# Crie um programa que tenha uma função chamada voto() que vai receber como 
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal 
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))