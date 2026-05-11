"""
Sequência de Fibonacci
Escreva um programa que leia um valor N e exiba todos os termos da sequência de Fibonacci menores
que N.
"""

limite = int(input())

fibonacci = 0
b = 1

while fibonacci <= limite:
    print(fibonacci)
    proximo = fibonacci + b
    fibonacci = b
    b = proximo