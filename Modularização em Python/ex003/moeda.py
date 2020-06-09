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
