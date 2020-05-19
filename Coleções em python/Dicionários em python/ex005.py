# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os 
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No 
# final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
people = list()
women = list()
person = dict()
average = 0
while True:
    person['name'] = str(input('Nome da pessoa: ')).strip()
    person['gender'] = str(input(f'Gênero de {person["name"]} [Masculino/Feminino]: ')).upper().strip()[0]
    while person['gender'] not in 'MF':
        print('ERRO! Por favor, digite um gênero válido')
        person['gender'] = str(input(f'Gênero de {person["name"]} [Masculino/Feminino]: ')).upper().strip()[0]
    if person['gender'] == 'F':
        women.append(person['name'])
    person['age'] = int(input(f'Idade de {person["name"]}: '))
    average += person['age']
    people.append(person.copy())
    choice = str(input('Quer adicionar mais pessoas ? [Sim/Não] ')).strip().lower()[0]
    while choice not in 'sn':
        print('ERRO! Por favor, digite uma opção válida')
        choice = str(input('Quer adicionar mais pessoas ? [Sim/Não] ')).strip().lower()[0]
    if choice == 'n':
        break
average /= len(people)
print('='*50)
print(f'A) Temos {len(people)} pessoas cadastradas')
print(f'B) A média de idade é de {average:.2f} anos ')
print(f'C) As mulheres cadastradas foram {women}')
print(f'D) Pessoas com idade acima da média: ')
for element in people:
    if element['age'] > average:
        print(f'     Nome: {element["name"]}; Gênero: {element["gender"]}; Idade: {element["age"]};')
print('\n<< ENCERRADO >>')