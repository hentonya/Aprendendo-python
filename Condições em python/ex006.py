'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários 
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
salário = float(input('Digite o salário do funcionário: R$ '))
if salário > 1250:
    print('O seu novo salário com um aumento de 10% é R$ {:.2f}'.format(10/100*salário+salário))
else:
    print('O seu novo salário com um aumento de 15% é R$ {:.2f}'.format(15/100*salário+salário))
