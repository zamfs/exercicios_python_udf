n = int(input('Digite o número de linhas: '))

for i in range(1, n+1):
    linha = ''
    num_asteriscos = (2*i) - 1
    num_espacos_esquerdas = n - i

    for _ in range(num_espacos_esquerdas):
        linha += ' '
    
    for _ in range(num_asteriscos):
        linha += '*'
    
    print(linha)