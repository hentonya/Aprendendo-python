def menu():
    print(60*'\033[m=')
    print(f'\033[1;31m{"MENU PRINCIPAL":^60}\033[m')
    print(60*'=')
    print('\033[1;33m1 - \033[1;94mVer pessoas cadastradas\033[m')
    print('\033[1;33m2 - \033[1;94mCadastar nova pessoa\033[m')
    print('\033[1;33m3 - \033[1;94mSair do sistema\033[m')
    print(60*'=')
def leiaInt(txt = ''):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[1;31mERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        else:
            return num

