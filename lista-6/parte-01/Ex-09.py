"""
Criando um conjunto e removendo duplicatas
Crie a lista numeros = [1, 3, 5, 3, 1, 7, 5, 9, 7]. Converta-a para um conjunto (set) para eliminar
duplicatas. Exiba o conjunto resultante e sua quantidade de elementos.
"""

numeros = [1, 3, 5, 3, 1, 7, 5, 9, 7]
print(f'Lista inicial: {numeros}')

numeros_set = set(numeros)

print(f'Set: {numeros_set}')

print(f'Tamanho do novo set: {len(numeros_set)}')
