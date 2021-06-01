''' Convertendo valores com o auxílio do try e do except'''

def convert_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
        
while True:
    numero = convert_numero(input('Digite um número: '))
    if numero is None:
        print('Erro: Isso não é um número.')
        break
    else:
        print(numero * 2)