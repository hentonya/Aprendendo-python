# Faça um programa que tenha uma função notas() que pode receber várias notas de 
# alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """    
    alunos = dict()
    alunos['total'] = len(nota)
    alunos['maior'] = max(nota)
    alunos['menor'] = min(nota)
    alunos['média'] = sum(nota)/len(nota)
    if sit == True:
        if alunos['média'] >= 9:
            alunos['situação'] = 'EXCELENTE'
        elif alunos['média'] >= 7:
            alunos['situação'] = 'ÓTIMO'
        elif alunos['média'] >= 5:
            alunos['situação'] = 'BOA'
        else:
            alunos['situação'] = 'RUIM'
    return alunos

#help(notas)
resp = notas(9,10,5.5,2.5,8.5,sit=True)
print(resp)