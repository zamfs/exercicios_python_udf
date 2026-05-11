"""
Cálculo de IMC: Leia o peso (kg) e a altura (m) de uma pessoa e calcule o seu IMC. (Fórmula: IMC = peso / (altura * altura)).
"""

peso = float(input())
altura = float(input())

imc = peso/(altura**2)

print(f'O imc é: {imc}')