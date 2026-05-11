"""
Ano bissexto (simplificado). Leia um ano e exiba "Ano bissexto!" se ele for divisível por 4 e (não
divisível por 100 ou divisível por 400).
"""

ano = int(input())

if ((ano % 4) == 0) and (((ano % 100) != 0) or ((ano % 400) == 0)):
    print('Ano bissexto!')