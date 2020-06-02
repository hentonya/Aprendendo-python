# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
# semelhante a função input() do Python, só que fazendo a validação para aceitar 
# apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')
def leiaInt(txt):
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            return int(num)
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')

    
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')