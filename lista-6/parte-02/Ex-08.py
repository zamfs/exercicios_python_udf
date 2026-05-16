"""
Contagem de frequência com dicionário
Dada a string frase = "banana", conte a frequência de cada letra usando um dicionário e o método
.get(). Exiba o resultado.
"""

contagem_letras = {}

frase = "banana"

for letra in frase:
    if letra not in contagem_letras:
        contagem_letras[letra] = 1
    else:
        contagem_letras[letra] += 1

print('Resultado')
for letra in sorted(set(frase)):
    print(f'{letra}: {contagem_letras.get(letra)}')