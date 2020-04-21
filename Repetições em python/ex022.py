# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido 
# quando o número solicitado for negativo
num = 0 
while True:
    num = int(input('\nDeseja ver a tabuada de multiplicação de qual número ? '))
    if num < 0:
        break
    for c in range (1,11):
        print(f'{num} x {c:2} = {num * c}')
print('\nPrograma encerrado')