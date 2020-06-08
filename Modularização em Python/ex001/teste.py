# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo 
# e use algumas dessas funções.
import moeda
preço = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos R${moeda.aumentar(preço,10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(preço,10)}')
print(f'O dobro de R${preço} é R${moeda.dobro(preço)}')
print(f'A metade de R${preço} é R${moeda.metade(preço)}')
