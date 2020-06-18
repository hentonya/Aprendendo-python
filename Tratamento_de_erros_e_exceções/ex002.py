# Crie um código em Python que teste se o site pudim está acessível pelo computador usado
from urllib import request, error

try:
    site = request.urlopen('http://pudim.com.br/')
except error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    