'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
'''

while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        print()
        if (numero % 2) == 0:
            print(f'{numero} é um número par')
        else:
            print(f'{numero} é um número ímpar')
        break
    except:
        print('Valor incorreto, por favor digite novamente!', '\n')

