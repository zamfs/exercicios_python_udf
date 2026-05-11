"""
Velocidade acima do limite. Leia a velocidade de um veículo (km/h). Se ultrapassar 80 km/h,
exiba "Velocidade acima do limite!".
"""

velocidade = float(input())

if velocidade > 80.0:
    print("Velocidade acima do limite!")