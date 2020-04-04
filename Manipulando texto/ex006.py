#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
frase = input('Digite seu nome completo: ').split()
print('Seu primeiro nome é {}'.format(frase[0].title()))
print('Seu último nome é {}'.format(frase[len(frase)-1].title())) 
