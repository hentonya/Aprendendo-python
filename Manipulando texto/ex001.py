#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')
print('Seu nome em letras maiúsculas: {}\nSeu nome em letras minúsculas: {}'.format(nome.upper(),nome.lower()))
print('O seu nome completo tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
nome = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(nome[0],len(nome[0])))
