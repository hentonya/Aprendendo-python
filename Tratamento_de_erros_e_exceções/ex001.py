# Reescreva a função leiaInt() , incluindo agora a possibilidade da digitação de 
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a 
# mesma funcionalidade
def leiaInt(txt = ''):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUSUÁRIO PREFERIU NÃO DIGITAR ESSE NÚMERO\033[m')
            return 0
        else:
            return num


def leiaFloat(txt = ''):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: POR FAVOR, DIGITE UM NÚMERO REAL VÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUSUÁRIO PREFERIU NÃO DIGITAR ESSE NÚMERO\033[m')
            return 0
        else:
            return num


num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')
