# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista 
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e 
# ímpares em ordem crescente
numbers = [[],[]]
for n in range (0,7):
    aux = int(input(f'Digite o {n+1}º valor: '))
    if aux % 2 == 0:
        numbers[0].append(aux)
    else:
        numbers[1].append(aux)
numbers[0].sort()
numbers[1].sort()
print(f'Os valores pares digitados foram: {numbers[0]}')
print(f'Os valores ímpares digitados foram: {numbers[1]}')