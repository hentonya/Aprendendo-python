# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(40*'=')
for k, v in aluno.items():
    print(f'- {k}: {v}')
