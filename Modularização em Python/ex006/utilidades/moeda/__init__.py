def aumentar(preço=0, taxa=0,formatar=False):
    res = preço + (taxa * preço/100)
    if formatar == True:
        return moeda(res)
    else:
        return res


def diminuir(preço=0, taxa=0, formatar=False):
    res = preço - (taxa * preço/100)
    if formatar == True:
        return moeda(res)
    else:
        return res


def dobro(preço=0, formatar=False):
    res = preço*2
    if formatar == True:
        return moeda(res)
    else:
        return res


def metade(preço=0, formatar=False):
    res = preço/2
    if formatar == True:
        return moeda(res)
    else:
        return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, taxa_a=10, taxa_r=5):
    print(40*'=')
    print('RESUMO DO VALOR'.center(40))
    print(40*'=')
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preço,taxa_a,True)}')
    print(f'{taxa_r}% de redução: \t{diminuir(preço,taxa_r,True)}')
    print(40*'=')

