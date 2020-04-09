'''Refaça o EXERCÍCIO 007 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes '''
a = float(input('Digite o comprimento 01: '))
b = float(input('Digite o comprimento 02: '))
c = float(input('Digite o comprimento 03: '))
if a < (b+c) and a > abs(b-c) and  b < (a+c) and b > abs(a-c) and  c < (a+b) and c > abs(b-a):
    if a == b == c:
        print('Essas três retas PODEM formar um TRIÂNGULO EQUILÁTERO !')
    elif b == c or b ==a or c == a:
        print('Essas três retas PODEM formar um TRIÂNGULO ISÓSCELES !')
    else:
        print('Essas três retas PODEM formar um TRIÂNGULO ESCALENO !')
else:
    print('Essas três retas NÃO PODEM formar um TRIÂNGULO !')
