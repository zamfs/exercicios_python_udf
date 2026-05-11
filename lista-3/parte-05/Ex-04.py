"""
Aproximação de PI (série de Leibniz)
Escreva um programa que calcule uma aproximação do valor de PI utilizando a série de Leibniz: PI/4
= 1 - 1/3 + 1/5 - 1/7 + 1/9 - ... O programa deve somar termos enquanto o valor absoluto do termo atual
for maior que 0.000001.
"""

divisor = 1
termo = 1/divisor
sinal = 1

soma = 0

while termo > 0.000001:
    termo = termo * sinal
    soma += termo

    divisor += 2
    sinal *= -1
    termo = 1/divisor

print(termo)