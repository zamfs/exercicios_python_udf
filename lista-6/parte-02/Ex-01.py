"""
Fatiamento com passo
Crie uma lista com os números de 0 a 20. Usando fatiamento com passo, exiba: os números pares
(passo 2 começando de 0), a lista invertida (passo -1) e os múltiplos de 5.
"""

numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(f'Números pares: {numeros[0::2]}')
print(f'Lista invertida: {numeros[::-1]}')
print(f'Múltiplos de 5: {numeros[5::5]}')