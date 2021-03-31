'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é muito grande".
'''

nome = input('Qual o seu nome?: ')
tamanho = len(nome)
if tamanho <= 4:
    print(f'Seu nome tem {tamanho} letras, e é um nome curto.')
elif tamanho <= 6:
    print(f'Seu nome tem {tamanho} letras, e é um nome normal.')
else:
    print(f'Seu nome tem {tamanho} letras, e é um nome muito grande.')
