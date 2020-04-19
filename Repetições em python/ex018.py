#Sequência de Fibonacci
n = int(input('Quantos termos você quer mostar ? ')) - 1
x = 1
y = 0
z = 0
print('0',end=' >> ')
while n > 0:
    print('{}'.format(x),end=' >> ')
    z = x + y
    y = x
    x = z
    n -= 1 
print('FIM')
