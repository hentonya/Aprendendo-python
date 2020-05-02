""" 
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela
"""
numbers = list()
for c in range (5):
    aux = int(input('Digite um número: '))
    if c == 0 or aux > numbers[-1]:
        numbers.append(aux)
        print('Número adicionado na última posição')
    else:
        for c1 in range (5):
            if aux <= numbers[c1]:
                numbers.insert(c1,aux)
                print(f'Número adicionado na posição {c1}')
                break
print(30*'-=')
print(f'Os valores digitados em ordem foram {numbers}')
