"""
Escreva um programa que percorra os números de 1 a 100 e exiba apenas os múltiplos de 7. Use
continue para pular os não múltiplos.
"""

for i in range(1,101):
    if i % 7 !=  0:
        continue
    print(i)