"""
Escreva um programa que gere e exiba os n primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3,
5, 8, 13, ...) utilizando um laço for.
"""

a = 0 #número atual da sequência
b = 1 #próximo número da sequência

termos = int(input('Quantos termos da sequência de fibonacci: '))

for _ in range(termos):
    print(a)
    a, b = b, a + b