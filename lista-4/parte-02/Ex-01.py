num_de_repeticoes = int(input('Quantas repetições? '))

maior = None
menor = None

for i in range(num_de_repeticoes):
    num = int(input('Digite um número: '))

    if maior == None and menor == None:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
print(f'Maior: {maior}\nMenor: {menor}')