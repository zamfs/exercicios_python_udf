"""
Velocidade Média: Um carro viajou entre duas cidades. Leia a distância percorrida (em km) e o tempo gasto (em horas).
Calcule e exiba a velocidade média do veículo
"""

km = float(input())
tempo = float(input()) #em horas

velMedia = km/tempo

print(f'Velocidade média: {round(velMedia, 2)} km/h')