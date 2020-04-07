'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento ? '))
prestação = valor / (12 * anos) 
if prestação > 30 / 100 * salário:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}\n\033[31mEMPRÉSTIMO NEGADO\033[m'.format(valor,anos,prestação))
else:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}\n\033[32mEMPRÉSTIMO APROVADO\033[m'.format(valor,anos,prestação))
