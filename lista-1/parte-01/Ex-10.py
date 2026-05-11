"""
Conversão de Temperatura: Escreva um algoritmo que leia uma temperatura em graus Celsius e a converta para
Fahrenheit (Fórmula: F = (C * 9/5) + 32).
"""

celsius = float(input())

conversao = ((celsius*(9/5))+32)

print(f'O valor em Farenheit: {conversao} °F')