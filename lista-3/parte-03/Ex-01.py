num = int(input('Digite um número entre 1 e 100: '))

while num < 1 or num > 100:
    print('Número inválido!')
    num = int(input('Digite um número entre 1 e 100: '))
print('Número válido!')