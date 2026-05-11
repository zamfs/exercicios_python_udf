"""
Consumo Médio de Combustível: Leia a distância total percorrida por um automóvel (km) e o total de combustível
consumido (litros). Calcule e exiba o consumo médio (km/l).
"""

km = float(input())
combustivel = float(input())

consumo = km/combustivel

print(f'O consumo foi de: {round(consumo,2)} km/L')