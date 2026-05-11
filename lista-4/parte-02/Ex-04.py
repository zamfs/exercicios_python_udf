"""
Escreva um programa que receba uma lista de palavras e exiba cada palavra junto com seu
comprimento, usando enumerate(). Formato:
1. Python (6 letras)
2. Programação (11 letras)
"""

palavras = ["Python", "Programação"]

for palavra in palavras:
    for index, letra in enumerate(palavra, start=1):
        if index == len(palavra):
            print(f'{palavra} ({index} letras)')