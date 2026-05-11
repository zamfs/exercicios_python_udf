"""
Sensação térmica. Leia a temperatura (°C) e classifique: Gelado (≤ 0), Frio (1–15), Agradável
(16–25), Quente (26–35) ou Muito quente (> 35).
"""

temperatura = float(input())

if temperatura >= 0 and temperatura < 1:
    print('Gelado')
elif temperatura <= 15:
    print('Frio')
elif temperatura <= 25:
    print('Agradável')
elif temperatura <= 35:
    print('Quente')
elif temperatura > 35:
    print('Muito quente')