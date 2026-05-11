"""
Jogo de adivinhação
Escreva um programa que defina um número secreto (fixo, por exemplo, 42) e peça ao usuário para
adivinhar. A cada tentativa, o programa deve informar se o palpite foi alto ou baixo. O laço termina
quando o usuário acerta, e o programa deve informar o total de tentativas.
"""

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