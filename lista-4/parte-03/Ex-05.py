"""
Escreva um programa que leia números do usuário em um laço for de 5 iterações. Se o número for
negativo, exiba "Valor negativo ignorado" e use continue. Se o número for 0, exiba "Zero encerra a
entrada" e use break. Caso contrário, acumule a soma dos valores.
"""

print('Soma de números. Números negativos são ignorados. O 0 encerra a execução.')

soma = 0

for _ in range(5):
    n = int(input('Digite um número: '))

    if n < 0:
        continue
    elif n == 0:
        break
    else:
        soma += n

print(f'Soma: {soma}')