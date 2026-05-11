"""
Utilizando for-else, escreva um programa que busque um valor em uma lista de números inteiros. Se o
valor for encontrado, exiba sua posição (índice) e interrompa com break. Se não for encontrado, o
bloco else deve informar que o valor não está na lista.
"""

numeros = [2,5,3,1,8,7,11]

n_pesquisado = int(input('Digite um número para pesquisar na lista: '))

for index, numero in enumerate(numeros):
    if n_pesquisado == numero:
        print(f'Encontrado! número: {numero} index -> {index}')
        break
else:
    print('Número não encontrado na lista!')