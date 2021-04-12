'''
Crie uma função que receba outra função como parâmetro e retorne o valor da segunda 
função executada. Faça a primeira função executar duas funções que recebam um número
diferente de argumentos.
'''

def principal(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def apresentacao(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

print(principal(apresentacao,'Cristina'))
print(principal(saudacao, 'Cristina', saudacao='Bom dia!'))