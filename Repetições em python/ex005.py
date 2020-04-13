#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
sum = 0
for c in range (0,6):
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        sum += number
print('A soma dos números inteiros pares é {}'.format(sum))
