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