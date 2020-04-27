"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo 
por extenso.
"""
nums = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','quatorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
escolha = int(input('Digite um número de 0 à 20: '))
while escolha not in range (0,21):
    escolha = int(input('Número inválido, tente novamente\nDigite um número de 0 a 20: '))
print(f'Você digitou o número {nums[escolha]}')


