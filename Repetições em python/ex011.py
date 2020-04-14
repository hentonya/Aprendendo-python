'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do 
homem mais velho e quantas mulheres têm menos de 20 anos.'''
md = 0
mul = 0 
hm = ''
ihm = 0
for c in range (1,5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    md += idade / 4
    if sexo == 'f' and idade < 20:
        mul += 1
    if sexo == 'm':
        if c == 1:
            hm = nome
            ihm = idade
        elif idade > ihm:
            ihm = idade
            hm = nome
        elif idade == ihm:
            hm += '/' + nome   
print('A média de idade do grupo é de {} anos'.format(md))
print('O homem mais velho tem {} anos e se chama {}'.format(ihm, hm))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mul))