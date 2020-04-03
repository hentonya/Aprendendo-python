#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o seu nome completo: ').strip()
print('{}'.format('silva' in nome.lower()))
