"""
Potências de 2
Escreva um programa que exiba todas as potências de 2 que sejam menores ou iguais a um valor limite
informado pelo usuário.
"""

limite = int(input())

n = 0
while 2**n <= limite:
    print(2**n)
    n+=1