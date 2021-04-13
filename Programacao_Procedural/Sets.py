'''
Sets (Conjuntos)
'''

# add (adiciona), update (atualiza), clear (limpar), discard (remove o elemento se ele estiver contido no set)   
# union | (todos os elementos presentes nos dois sets, valores duplicados são excluídos)
# intersection & (somente os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, são elementos que estão em um set ou no outro, mas não em sua interseção)

conjunto_1 = {1,2,3,4,5,6,7,8,9}
conjunto_2 = {1,2,3,4,5,6,7,8,9,10}

uniao = conjunto_1.union(conjunto_2)
print(f'A união dos dois conjuntos resulta em: {uniao}\n')

intersecao = conjunto_1.intersection(conjunto_2)
print(f'A interseção dos dois conjuntos resulta em: {intersecao}\n')

diferenca = conjunto_1.difference(conjunto_2)
print(f'A diferença dos dois conjuntos resulta em: {diferenca}\n')

diferenca_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print(f'A diferença simétrica dos dois conjuntos resulta em: {diferenca_simetrica}\n')

