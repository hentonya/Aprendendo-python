#Refaça o exercício 006, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
cont = 0
while cont < 10:
    print(num1,end = ' → ')
    num1+= num2
    cont += 1
print('Fim')
