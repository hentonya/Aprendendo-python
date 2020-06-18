# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um 
# arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas 
# as pessoas cadastradas.
from Tratamento_de_erros_e_exceções.ex003.lib.arquivo import *
from Tratamento_de_erros_e_exceções.ex003.lib.interface import *
arq = 'pessoas.txt'
if not existeArquivo(arq):
    criarArquivo(arq)
while True:
    menu()
    while True:
        escolha = leiaInt('\033[1;33mSua opção:\033[1;92m ')
        if escolha not in range(1,4):
            print('\033[1;31mERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        else:
            break
    if escolha == 3:
        print(60*'\033[m=')
        print(f'\033[1;31m{"PROGRAMA ENCERRADO":^60}\033[m')
        print(60*'=')
        break
    if escolha == 1:
        lerArquivo(arq)
    if escolha == 2:
        print(60 * '\033[m=')
        print(f'\033[1;31m{"NOVO CADASTRO":^60}\033[m')
        print(60 * '=')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

