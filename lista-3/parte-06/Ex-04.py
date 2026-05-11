"""
Colisão de populações
A cidade A possui 80.000 habitantes e cresce 3% ao ano. A cidade B possui 200.000 habitantes e
cresce 1,5% ao ano. Escreva um programa que calcule em quantos anos a população de A ultrapassará
a de B. Caso A nunca ultrapasse B em até 500 anos, informe essa condição.
"""

A = 80000
B = 200000

anos = 0

while A <= B and anos <= 500:
    anos += 1
    A = A*1.03
    B = B*1.015

if anos > 500:
    print('Ultrapassou 500 anos!')
else:
    print(f'A cidade A ultrapassou a cidade B em: {anos} anos.')