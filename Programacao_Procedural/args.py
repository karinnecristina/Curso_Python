'''
Crie uma função que recebe outra função como parâmetro e retorne 
o valor da segunda função executada.
'''

def funcao1():
    return 'Trabalhando com funções'

def funcao2(args):
    return args()

print(funcao1())
