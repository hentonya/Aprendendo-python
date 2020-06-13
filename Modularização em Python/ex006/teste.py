# Dentro do pacote utilidades que criamos no exercício 005, 
# temos um módulo chamado dado. Crie uma função chamada 
# leiaDinheiro que seja capaz de funcionar como a função 
# input, mas com uma validação de dados para aceitar apenas 
# valores que seja monetários
from utilidades import moeda,dado
preço = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preço,35,22)
