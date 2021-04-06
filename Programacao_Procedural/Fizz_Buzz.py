''' Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado. 
'''
from random import randint

def fizzbuzz(numero):
    if (numero % 5) == 0 and (numero % 3) == 0:
        return f'fizzbuzz, {numero} é divisível por 3 e 5'
    if numero % 5 == 0:
        return f'fizz, {numero} é divisível por 5'
    if numero % 3 == 0:
        return f'buzz, {numero} é divisível por 3'
    return f'O número enviado foi {numero}'

for valor in range(5):
    valor_aleatorio = randint(0,100)
    print(fizzbuzz(valor_aleatorio))
