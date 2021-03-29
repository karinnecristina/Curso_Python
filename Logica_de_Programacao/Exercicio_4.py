'''
Primeira calculadora

observação: Esse exercício será aprimorado ao longo das aulas.
'''

while True:
    print(f'#' * 56)
    print(f'Essa calculadora executa cálculos básicos (+, -, * e /)')
    print(f'#' * 56,'\n')

    valor_1 = input('Digite o primeiro valor: ')
    valor_2 = input('Digite o segundo valor: ')
    operador = input('Digite um operador: ')
    print()

    if not valor_1.isnumeric() or not valor_2.isnumeric():
        print(f'O cálculo não foi realizado, um dos valores informado não é um número, repita a operação com um valor válido.','\n')
        continue

    valor_1 = int(valor_1) 
    valor_2 = int(valor_2)

    if operador == '+':
        print(f'\nO resultado da sua operação é: {valor_1 + valor_2}\n')
    elif operador == '-':
        print(f'\nO resultado da sua operação é: {valor_1 - valor_2}\n')
    elif operador == '*':
        print(f'\nO resultado da sua operação é: {valor_1 * valor_2}\n')
    elif operador == '/':
        print(f'\nO resultado da sua operação é: {valor_1 / valor_2}\n')
    else:
        print(f'Operador inválido','\n')

    sair = input('Gostaria de realizar uma novo cálculo? [s]im ou [n]ão: ')
    print()
    if sair != 's':
        break