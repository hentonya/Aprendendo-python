'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''
preço = float(input('Digite o preço do produto:\nR$ '))
forma = int(input(('\n[1] À vista dinheiro/cheque\n[2] À vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão\n\nInforme a condição de pagamento: ')))
if forma == 1:
    print('Sua compra de R$ {:.2f} irá custar R$ \033[31m{:.2f}\033[m com 10% de desconto\n'.format(preço , preço - 10/100*preço ))
elif forma == 2:
    print('Sua compra de R$ {:.2f} irá custar R$ \033[31m{:.2f}\033[m com 5% de desconto\n'.format(preço , preço - 5/100*preço ))
elif forma == 3:
    print('Sua compra de R$ \033[31m{:.2f}\033[m será parcelada em \033[31m2x sem juros\033[m de R$ \033[31m{:.2f}\033[m\n'.format(preço ,preço / 2))
elif forma == 4:
    num = int(input('Digite o número de parcelas: '))
    print('Sua compra de R$ {:.2f} irá custar R$ \033[31m{:.2f} com 20% de juros\033[m. Sua compra será parcelada em \033[31m{}x\033[m de R$ \033[31m{:.2f}\033[m\n'.format(preço, preço + 20/100*preço , num, (preço + 20/100*preço )/num))
else:
    print('\033[31mCondição de pagamento inválida\033[m')




