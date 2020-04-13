#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
for c in range (1,11):
    print(num1,end = ' >> ')
    num1+= num2
print('Fim')
