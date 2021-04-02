# ===========================================
# Validador de CPF

# Multiplicar cada dígito por cada valor de um range de 10 a 2 (em ordem decrescente).
## Obervação: toda essa operação deve ser feita sem considerar os dois últimos dígitos.
# Somar todos os resultados da multiplicação anterior.

# Fórmula:
# número de dígitos - (soma da multiplicação % 11)
# Se o resultado da operação anterior for maior que nove o décimo dígito será 0 caso contrário será o próprio resultado.
# Para o próximo dígito é a mesma coisa, a diferença é que precisamos incluir esse dígito 
# no processo da multiplicação que foi feito no início do programa,
# outro detalhe é que o range agora deve iniciar em 11. 

# Vamos usar um CPF aleatório para verificar o funcionamento do nosso programa.

# =========================================== 


while True:

    CPF = input('Digite seu CPF: ')
    # Verificando se o número de dígitos do CPF está correto:
    if len(CPF) == 11:
        pass
    else:
        print(f'Você digitou {len(CPF)} caracteres, seu CPF deve conter 11 dígitos.') 
        break

    validador = CPF[:-2] # Obtendo os 9 primeiros dígitos
    reverso = 10         # Contador reverso
    total = 0
   
    # Faz todo o cálculo: 
    for index in range(19):
        if index > 8:  # Primeiro índice vai de 0 a 9
            index -= 9 # São os 9 primeiros dígitos do CPF

        total += int(validador[index]) * reverso # Valor total da multiplicação
        
        reverso -= 1 # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)
            if digito > 9: # Se o dígito for maior que 9 o valor é 0
                digito = 0
            total = 0 # Zera o total 
            validador += str(digito) # Concatena o dígito gerado no novo CPF

    # Se for digitado uma sequêcia como 11111111111 ou 00000000000, ......
    # O CPF será considerado válido, então vamos tratar esse problema:
    sequencia = validador == str(validador[0]) * len(CPF)
    if CPF == validador and not sequencia:
        print('Esse CPF é válido.')
    else:
        print('Esse CPF não é válido.')
    
    # Encerrando o programa:
    sair = input('Gostaria de testar um novo CPF? [s]im ou [n]ão: ')
    print()
    if sair != 's':
        break

            