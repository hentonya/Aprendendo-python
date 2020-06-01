# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o 
# primeiro que indique o número a calcular e outro chamado show, que será um valor 
# lógico (opcional) indicando se será mostrado ou não na tela o processo de 
# cálculo do fatorial.
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de num.
    :param num : O valor a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de num.
    """  
    fat = 1
    for c in range(num,0,-1):
        if show:
            print(f'{c} x ' if c > 1 else f'{c} = ',end='')
        fat *= c
    return fat


#help(fatorial)
n = int(input('Digite um número: '))
print(fatorial(n,True))
