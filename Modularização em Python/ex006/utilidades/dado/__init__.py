def leiaDinheiro(txt=''):
    preço = str(input(f'{txt}')).replace(',','.').strip()
    while not preço.replace('.','').isnumeric():
        preço = str(input(f'\033[1;31mErro: "{preço}" é um preço inválido!\033[m\n{txt}')).replace(',','.').strip()
    return float(preço)
 