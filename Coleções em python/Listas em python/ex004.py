# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numbers = list()
while True:
    numbers.append(int(input('Digite um número: ')))
    auxiliar = ' ' 
    while auxiliar not in 'sn':
        auxiliar = str(input('Deseja continuar ? [Sim/Não] ')).lower().strip()[0]
    if auxiliar == 'n':
        break
print(f'Quantidade de números que foram digitados: {len(numbers)}')
numbers.sort(reverse=True)
print(f'Números digitados em ordem decrescente: {numbers}')
if 5 in numbers:
    print('O número 5 faz parte da lista !')
else:
    print('O número 5 não foi encontrado na lista !')
