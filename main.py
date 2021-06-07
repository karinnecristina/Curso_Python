from vendas.calcula_preco import aumento, reducao
from vendas.formata import formata_preco

preco = 39.90
preco_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_aumento)

preco_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_reducao)