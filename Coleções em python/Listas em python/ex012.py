# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
# notas de cada aluno individualmente.
alunos = list ()
aux = list ()
while True:
    aux.append(str(input('Nome: ')).strip().capitalize())
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    alunos.append(aux[:])
    aux.clear()
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja continuar ? [Sim/Não] ')).strip().lower()[0]
    if escolha == 'n':
        break
print()
print(30*'-')
print(f'{"Nº":<}{"Nome":^23}{"Média":>}')
print(30*'-')
for pos, cont in enumerate(alunos):
    print(f'{pos:<}{cont[0]:^25}{(cont[1] + cont[2])/2:>.1f}')
print(30*'-')
print()
while True:
    print()
    num = int(input('Mostrar as notas de qual aluno? (999 interrompe) '))
    if num == 999:
        break
    if num not in range(0,len(alunos)):
        print(f'O aluno {num} não existe!')
    else:
        print(f'Notas de {alunos[num][0]} são {alunos[num][1:]}')
print()
print('Programa encerrado')