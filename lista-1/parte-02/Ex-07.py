"""
Juros Simples: Leia um valor de capital, uma taxa de juros mensal (em porcentagem) e o tempo em meses. Calcule os
juros rendidos e o valor final (Capital + Juros).
"""

capital = float(input())
taxa = float(input())
tempo = float(input()) #meses

capital_final = (capital*taxa*tempo) + capital

print(f'Juros rendidos: R${capital_final-capital}\nRendimento final: R${capital_final}')