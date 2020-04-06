#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
if num1 > num2 and num1 > num3:
    print('O maior valor digitado foi {}'.format(num1))
    if num2 < num3:
        print('O menor valor digitado foi {}'.format(num2))
    else:
        print('O menor valor digitado foi {}'.format(num3))                     
if num2 > num1 and num2 > num3:
    print('O maior valor digitado foi {}'.format(num2))
    if num1 < num3:
        print('O menor valor digitado foi {}'.format(num1))
    else:
        print('O menor valor digitado foi {}'.format(num3))
if num3 > num1 and num3 > num2:
    print('O maior valor digitado foi {}'.format(num3))
    if num1 < num2:
        print('O menor valor digitado foi {}'.format(num1))
    else:
        print('O menor valor digitado foi {}'.format(num2)) 
        