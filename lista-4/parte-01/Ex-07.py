"""
Faça um programa que calcule e exiba o fatorial de um número inteiro positivo n fornecido pelo
usuário, utilizando um laço for.
"""

n = int(input('Digite um número: '))
fatorial = 1

for num in range(n,0,-1):
    fatorial *= num

print(fatorial)