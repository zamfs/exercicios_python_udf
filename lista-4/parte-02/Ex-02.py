num_de_repeticoes = int(input('Quantas repetições? '))

positivo = 0
negativo = 0
zeros = 0

for i in range(num_de_repeticoes):
    num = int(input('Digite um número: '))

    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        zeros += 1

print(f'Positivos: {positivo}\nNegativos: {negativo}\nZeros: {zeros}')