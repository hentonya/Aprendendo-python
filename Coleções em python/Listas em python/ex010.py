# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = []
pares = soma = 0
for linha in range (0,3):
    aux = []
    for coluna in range (0,3):
        aux.append(int(input(f'Digite um valor para [{linha},{coluna}]: ')))
        if aux[coluna] % 2 == 0:
            pares += aux[coluna]
        if coluna == 2:
            soma += aux[coluna]
    matriz.append(aux)
print(40*'*')
for linha in range (0,3):
    for coluna in range (0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(40*'*')
print(f'Soma de todos os valores pares digitados: {pares}')
print(f'Soma dos valores da terceira coluna: {soma}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
