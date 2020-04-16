'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto'''
sexo = str(input('Informe o seu sexo: [M/F]  ').lower().strip()[0])
while sexo not in 'mf':
    sexo = input('Opção inválida\nInforme novamente o seu sexo: [M/F]  ').lower().strip()[0]
print('Sexo {} registrado com sucesso'.format('masculino' if sexo =='m' else 'feminino'))
