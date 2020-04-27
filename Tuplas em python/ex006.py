"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve 
mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ',end=' ')
    for c in range(0, len(palavra)):
        if  palavra[c] in 'AEIOU':
            print(palavra[c],end=' ')
