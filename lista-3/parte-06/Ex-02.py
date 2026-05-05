numero_secreto = 51
numero_tentativas = 1 #pois o usuário já irá fazer a primeira tentativa

entrada = int(input('Adivinhe o número: '))

while entrada != numero_secreto:
    numero_tentativas += 1
    if entrada > numero_secreto:
        print('Seu número é maior do que o número secreto.')
        entrada = int(input('Adivinhe o número: '))
    else:
        print('Seu número é menor do que o número secreto.')
        entrada = int(input('Adivinhe o número: '))

print('Acertou o número! Parabéns!')
print(f'Número de tentativas: {numero_tentativas}')