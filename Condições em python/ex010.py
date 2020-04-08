''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O \033[31mPRIMEIRO\033[m valor é maior')
elif b > a:
    print('O \033[31mSEGUNDO\033[m valor é maior')
else:
    print('Não existe valor maior, os dois são \033[31mIGUAIS\033[m')
