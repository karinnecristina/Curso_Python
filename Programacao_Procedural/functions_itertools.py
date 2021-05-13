from itertools import  combinations, permutations, product

pessoas = ['Luiz','Márcia','José','Marcos','Giovana','Daniela']

# Formando grupos de 2 pessoas:
for grupo in combinations(pessoas, 2): # Na combinação a ordem não importa e os valores únicos não se repetem
    print (grupo)

for grupo in permutations(pessoas, 2): # Na permutação a ordem é importante e os valores únicos não se repetem
    print (grupo)

for grupo in product(pessoas, repeat=2): # No produto a ordem é importante e os valores únicos se repetem
    print (grupo)

