#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase) 
inverso = frase[::-1]
print('A frase {} de trás para frente é {}'.format(frase, inverso))
if frase == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
