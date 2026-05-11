"""
Tabuada de um número
Escreva um programa que leia um número inteiro e exiba sua tabuada de multiplicação de 1 a 10.
"""

num = int(input())

mult = 1
while mult <= 10:
    print(num*mult)
    mult+=1