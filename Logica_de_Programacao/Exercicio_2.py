'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 
e Boa noite 18-23.
'''

while True:
    try:
        hora = int(input('Que horas são (0-23): '))
        if hora < 0 or hora > 23:
            print(f'A hora deve estar entre 0 e 23!')
        else:
            if hora <= 11:
                print(f'Bom dia!')
            elif hora <= 17:
                print(f'Boa tarde!')
            else:
                print(f'Boa noite!')
        break
    except:
        print(f'Por favor, digite um horário de 0 a 23.')

