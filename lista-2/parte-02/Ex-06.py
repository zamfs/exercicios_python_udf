"""
Febre ou normal. Leia a temperatura corporal (em °C) e informe se a pessoa está com febre
(acima de 37,5 °C) ou com temperatura normal.
"""

temperatura = float(input())

if temperatura > 37.5:
    print('Está com febre!')
else:
    print('Temperatura nornmal!')

    