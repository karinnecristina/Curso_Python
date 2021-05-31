''' Exemplo de exceções: '''

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))

def divide (valor_1, valor_2):
    if valor_2 == 0:
        raise ValueError
    return valor_1 / valor_2
try:
    print(int(divide(valor_1, valor_2)))
except ValueError as error:
    print('Você está tentando fazer uma divisão por zero, por favor tente outro valor.')
