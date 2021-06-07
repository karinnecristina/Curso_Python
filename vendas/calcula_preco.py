''' Funções para o cálculo de preços'''

from vendas.formata import formata_preco

def aumento(valor, porcentagem, formata=False):
    resultado = valor + (valor * (porcentagem / 100))
    if formata:
        return formata_preco.format_real(resultado)
    else:
        return resultado

def reducao(valor, porcentagem, formata=False):
    resultado = valor - (valor * (porcentagem / 100))
    if formata:
        return formata_preco.format_real(resultado)
    else:
        return resultado