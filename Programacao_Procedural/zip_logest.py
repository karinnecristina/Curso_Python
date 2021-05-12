'''
Podemos usar zip para unir 2 listas o problema é que essa função só une as listas até o tamanho da menor lista,
para solucionar esse problema podemos usar o zip_longest para capturar os valores da lista maior, como no exemplo abaixo:
'''

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # fillvalue=0 preenche a lista menor com zeros 
                                                                            # e a conta é realizada sem retornar erros no programa. 
print(lista_soma) 