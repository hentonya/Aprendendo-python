# Modifique as funções que form criadas no exercício 001 para que elas aceitem um 
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não 
# formatado pela função moeda(), desenvolvida no exercício 002.
import moeda
preço = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {moeda.aumentar(preço,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preço,13,True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço,True)}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço,True)}')
 