"""
Conversão de Minutos: Leia uma quantidade de tempo inteira expressa apenas em minutos. Transforme e exiba esse
valor convertido para Horas e Minutos restantes (Ex: 130 min = 2h e 10min).
"""

minutos = int(input())

horas = minutos // 60

print(f'{horas}h {minutos%60}min')