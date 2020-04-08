'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2)/2
if 5.0 <= med <= 6.9:
    print('Tirando {} e {}, a média do aluno é {:.1f}\nO aluno está em \033[31mRECUPERAÇÃO\033[m'.format(n1,n2,med))
elif med < 5.0:
    print('Tirando {} e {}, a média do aluno é {:.1f}\nO aluno está \033[31mREPROVADO\033[m'.format(n1,n2,med))
else:
    print('Tirando {} e {}, a média do aluno é {:.1f}\nO aluno está \033[32mAPROVADO\033[m'.format(n1,n2,med))
     