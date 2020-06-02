# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai 
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 
# 'FIM', o programa se encerrará.
while True:
    print(30*'=')
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print(30*'=')
    x = str(input('Função ou Biblioteca > ')).strip().lower()
    if x == 'fim':
        break
    help(x)
print(30*'=')
print(f'{"ATÉ LOGO":^30}')
print(30*'=')