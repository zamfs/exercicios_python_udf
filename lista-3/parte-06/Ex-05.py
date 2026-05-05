num = int(input('Digite um número para saber se ele é palíndromo. Digite 0 para parar: '))

num_palindromos = 0


while num != 0:

    numero = num
    numero_invertido = 0

    while numero > 0:
        numero_invertido = numero_invertido * 10 + numero % 10
        numero = numero // 10
        
    if numero_invertido == num:
        print(f'É palíndromo: {numero_invertido} = {num}')
        num_palindromos += 1
    else:
        print(f'Não é palíndromo: {numero_invertido} != {num}')
    
    num = int(input('Digite um número para saber se ele é palíndromo. Digite 0 para parar: '))

print(f'Total de palíndromos: {num_palindromos}')