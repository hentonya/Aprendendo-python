#Faça uma tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
number = int(input('Digite um número para ver a sua tabuada de multiplicação: '))
for c in range (1,11):
    print('{} x {:2} = {} '.format(number,c,c*number))
