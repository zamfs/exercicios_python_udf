"""
Crie um programa que percorra os números de 1 a 50 e encontre o primeiro número divisível por 3 e
por 5 simultaneamente. Ao encontrá-lo, exiba-o e interrompa o laço com break.
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        break