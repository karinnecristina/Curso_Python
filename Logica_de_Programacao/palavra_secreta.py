'''
Crie um jogo onde o usuário tenha que acertar qual é a palavra secreta, 
ele terá 3 chances e deve digitar uma letra por vez (números não devem ser aceitos). 
'''

palavra = 'empatia'
letras_digitadas = []
vidas = 3

while True:
    if vidas <= 0:
        print(f'Você perdeu!!','\n')
        break
        
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print(f'Você só pode digitar uma letra por vez.')
        continue

    letras_digitadas.append(letra)
  
    if letra in palavra:
        print(f'uhulll, a letra "{letra}" existe na palavra secreta.','\n')

    else:      
        print(f'aahhhh, a letra "{letra}" não existe na palavra secreta.','\n')
        letras_digitadas.pop()
        vidas -=1
        if vidas == 2:
            print(f'Você ainda tem {vidas} vidas.','\n')
        elif vidas == 1:
            print(f'Você ainda tem {vidas} vida.','\n')
        else:
            print(f'Que pena suas vidas acabaram :(')

    palavra_temporaria = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_digitadas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra:
        print(f'Parabéns, você GANHOU!!! A palavra era -> "{palavra_temporaria.upper()}"')
        break
    else:
        print(f'{palavra_temporaria}')