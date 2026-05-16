"""
List comprehension
Usando list comprehension, crie: (a) uma lista com os quadrados de 1 a 10; (b) uma lista apenas com
os números pares de 1 a 20; (c) uma lista com as letras da palavra "Python" em maiúsculas.
"""

quadrados = [n**2 for n in range(1,11)]
print(quadrados)

pares = [n for n in range(1,21) if n % 2 == 0]
print(pares)
