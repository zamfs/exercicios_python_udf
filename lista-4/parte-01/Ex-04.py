"""
Escreva um programa que leia um número inteiro n do usuário e exiba a tabuada desse número (de 1 a
10), no formato n x i = resultado.
"""

n = int(input('Digite um número: '))

for i in range(1,11):
    print(f'{n} x {i} = {n*i}')