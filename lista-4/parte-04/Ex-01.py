"""
Escreva um programa que leia números inteiros do usuário em um laço. Use try-except com continue
para ignorar entradas inválidas (não numéricas). Quando o usuário digitar -1, encerre com break. Ao
final, exiba a soma e a quantidade de números válidos digitados.
"""

print('Soma de números. Digite -1 para encerrar.')
soma = 0

while True:
    try:
        n = int(input('Digite um núemero: '))

        if n == -1:
            break
        else:
            soma += n

    except ValueError:
        print('Entrada inválida!')
        continue

print(f'Soma: {soma}')