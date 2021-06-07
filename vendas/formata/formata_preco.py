'''Padronizando o preço'''

def format_real(valor):
    return f'R$ {valor:.2f}'.replace('.',',')