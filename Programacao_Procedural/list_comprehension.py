'''
Trabalhando com List Comprehension
'''

lista = list(range(100))
output_1 = [valor for valor in lista if valor % 3 == 0 if valor % 8 == 0] # Trabalhando com 2 if
output_2 = [valor if valor % 3 == 0 and valor % 8 == 0 else '_' for valor in lista] # Trabalhando com if e else
print(output_1, end='\n')
print(output_2)

## Exercicio:

string = '01234567890123456789012345678901234567890123456789'
passo = 10
comp = [string[i:i + 10] for i in range(0, len(string), passo)]
result = '.'.join(comp)
print(result)