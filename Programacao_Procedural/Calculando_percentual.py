''' Crie una função que receba 2 números. O primeiro é um valor
e o segundo um percentual ex:(10%). Retorne o valor do primeiro número somado 
do aumento do percentual do mesmo.
'''

def aumento_percentual(valor, percentual):
    return (valor + (valor * percentual / 100))

resultado = aumento_percentual(10,10)
print(resultado)