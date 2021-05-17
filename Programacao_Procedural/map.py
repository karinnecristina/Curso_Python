'''Lista de produtos'''

produtos = [
    {'Nome':'Pera', 'Preco':5.00},
    {'Nome':'Uva', 'Preco':3.80},
    {'Nome':'Maçã', 'Preco':6.50},
    {'Nome':'Abacaxi', 'Preco':2.25},
    {'Nome':'Laranja', 'Preco':1.10},
    {'Nome':'Abacate', 'Preco':4.72}
]

'''Função que aumenta o preço do produto em 5%'''

def aumenta_preco(p):
    p['Preco'] = round(p['Preco'] * 1.05, 2) # round - usado para arredondar o preço para 2 casas decimais
    return p

'''Aplicando a função na lista de produtos '''

novo_preco = map(aumenta_preco, produtos) # A função map vai aplicar a função aumenta preço a cada item da lista de produtos
for produto in novo_preco:
    print(produto)
