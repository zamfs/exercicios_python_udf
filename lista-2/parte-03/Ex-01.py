"""
Classificação por nota (conceito). Leia a nota (0 a 10) e exiba o conceito: A (≥ 9), B (≥ 7), C (≥
5), D (≥ 3) ou F (abaixo de 3).
"""

nota = float(input())

if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('F')