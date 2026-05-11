"""
Quantidade de dígitos
Escreva um programa que leia um número inteiro positivo e informe quantos dígitos ele possui. Utilize
divisões sucessivas por 10.
"""

num = int(input())

contagem_digitos = 0

continuar = True

while continuar == True:
    num = num // 10
    if num > 0:
        contagem_digitos += 1
    else:
        contagem_digitos += 1
        continuar = False

print(contagem_digitos)