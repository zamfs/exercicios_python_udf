"""
MDC (Algoritmo de Euclides)
Escreva um programa que leia dois números inteiros positivos e calcule o Máximo Divisor Comum
(MDC) entre eles utilizando o algoritmo de Euclides.
"""

num1 = int(input())
num2 = int(input())

dividendo = 1
divisor = 1

if num1 != 0 and num2 != 0:
    if num1 > num2:
        dividendo = num1
        divisor = num2
    else:
        dividendo = num2
        divisor = num1

    resto = dividendo % divisor
    
    while resto != 0:
        dividendo = divisor
        divisor = resto

        resto = dividendo % divisor

    print('MDC: ', divisor)        

    
