# Adapte o código do desafio anterior, criando uma função adicional chamada moeda
# que consiga mostrar os números como um valor monetário formatado.
import moeda
preço = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço,10))}')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(preço,10))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')