"""
Escreva um programa que percorra uma lista de palavras e exiba apenas aquelas que possuem mais de
5 caracteres. Use continue para pular as palavras curtas.
"""

palavras  = ["sol", "computador", "lua", "programação", "oi", "Python", "algoritmo"]

for palavra in palavras:
    if len(palavra) <= 5:
        continue
    print(palavra)