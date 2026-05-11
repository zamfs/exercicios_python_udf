"""
Números pares em um intervalo
Escreva um programa que leia dois números inteiros A e B (A < B) e exiba todos os números pares
existentes no intervalo [A, B].
"""

a = int(input())
b = int(input())

while a <= b:
    if (a % 2) == 0:
        print(a)
    a += 1 