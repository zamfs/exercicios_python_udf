print('Digite 999 para parar.')
num = int(input('Digite um número: '))

numero_de_zeros = 0
numero_de_positivos = 0
numeros_de_negativos = 0

while num != 999:
    if num == 0:
        numero_de_zeros += 1
    elif num > 0:
        numero_de_positivos += 1
    else:
        numeros_de_negativos += 1
    num = int(input('Digite um número: '))

print(f'Zeros: {numero_de_zeros}. Positivos: {numero_de_positivos}. Negativos: {numeros_de_negativos}.')
