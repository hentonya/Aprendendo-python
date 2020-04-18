'''Melhore o exercício 016, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer 
mostrar 0 termos'''
num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
cont = 0
aux = 0
sum = 0
while cont < 10:
    print(num1,end = ' → ')
    num1+= num2
    cont += 1
    if cont == 10:
       aux = int(input('PAUSA\nQuantos termos você quer mostrar a mais ? '))
       cont -= aux
    sum += 1
print('Progressão finalizada com {} termos mostrados'.format(sum))