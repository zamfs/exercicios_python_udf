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