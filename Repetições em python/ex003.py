#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
aux = 0
cont = 0
for c in range (3,501,6):
        aux += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, aux))
