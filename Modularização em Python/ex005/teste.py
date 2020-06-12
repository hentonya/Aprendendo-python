# Crie um pacote chamado utilidades que tenha dois módulos 
# internos chamados moeda e dado. Transfira todas as funções 
# utilizadas nos exercícios 001, 002, 003 e 004 para o 
# primeiro pacote e mantenha tudo funcionando.
from utilidades import moeda
preço = float(input('Digite o preço: R$'))
moeda.resumo(preço,35,22)
   