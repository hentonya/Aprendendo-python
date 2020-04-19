'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o 
maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
média = contador = maior = menor = 0
repete = True 
while repete:
    número = int(input('Digite um número: '))
    if contador == 0:
        maior = menor = número
    elif número > maior:
        maior = número
    elif número < menor:
        menor = número
    contador += 1 
    média += número
    escolha = str(input('Deseja continuar ? [S/N] ')).lower().strip()[0]
    if escolha == 'n':
        repete = False
média /= contador
print('você digitou {} números e a média foi {}\nO maior valor foi {} e o menor foi {}'.format(contador,média,maior,menor))     
