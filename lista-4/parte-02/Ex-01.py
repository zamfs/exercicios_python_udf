"""
Faça um programa que leia n números fornecidos pelo usuário e determine o maior e o menor valor
digitado. Use o padrão de acumulação com for, inicializando maior e menor como None.
"""

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