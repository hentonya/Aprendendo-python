''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo 
com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''
massa = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em m: '))
imc = (massa) / (altura**2)
print('O seu IMC é {:.1f} '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc < 25:
    print('PARABÉNS\nVocê está com o PESO IDEAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')

    