'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para 
binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Digite um número inteiro: '))
aux = int(input('Escolha uma das bases para conversão:\n[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL\nSua opção: '))
if aux == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif aux == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif aux == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida')
