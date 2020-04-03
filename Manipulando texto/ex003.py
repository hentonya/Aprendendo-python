#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Em que cidade você nasceu ? ').lower().split()
print('{}'.format(('santo' == cidade[0]) or ('santo-' in cidade[0])))