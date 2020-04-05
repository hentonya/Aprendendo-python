'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 
200Km e R$0,45 para viagens mais longas.'''
num = float(input('Digite a distância da viagem em km: '))
if num <= 200:
    print('O preço a pagar pela passagem é R${:.2f}'.format(num*0.50))
else:
    print('O preço a pagar pela passagem é R${:.2f}'.format(num*0.45))
