'''Pegando o tempo que uma função demorou para executar'''

from time import time

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna

@velocidade
def tempo():
    for n in range(10):
        print(n, end='')
        
tempo()