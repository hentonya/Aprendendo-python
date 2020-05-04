# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo 
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressão = str(input('Digite a expressão: ')).strip()
validade = True
aux = 0 # Indica a quantidade de parênteses que devem ser fechados 
if expressão.count( '(' ) == expressão.count( ')' ):
    for caractere in expressão:
        if caractere == ')' and aux == 0:
            validade = False
            break
        if caractere == '(':
            aux += 1
        if caractere == ')':
            aux -= 1 
else:
    validade = False
if validade == False:
    print('Expressão inválida!')
else:
    print('Expressão válida!')