"""
Fatorial
Escreva um programa que leia um número inteiro não negativo N e calcule seu fatorial (N!) utilizando
while.
"""

num = int(input())
fatorial = 1

while num >= 1: 
    fatorial *=num
    num -=1

print(fatorial)