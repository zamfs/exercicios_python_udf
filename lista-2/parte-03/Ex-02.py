"""
Classificação de IMC. Leia peso (kg) e altura (m), calcule o IMC e classifique: Abaixo do peso (<
18,5), Normal (18,5–24,9), Sobrepeso (25–29,9) ou Obesidade (≥ 30).
"""

peso = float(input('Peso em Kg: '))
altura = float(input('ALtura em m: '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')