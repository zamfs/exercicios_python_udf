"""
Somatório de ímpares
Escreva um programa que leia um número inteiro positivo N e calcule a soma de todos os números
ímpares de 1 até N.
"""

N = int(input())

soma = 0
num_impar = 1

while num_impar < N:
    soma += num_impar
    num_impar += 2

print(soma)