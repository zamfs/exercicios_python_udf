"""
 Área e Perímetro de Retângulo: Faça um algoritmo que leia a base e a altura de um retângulo. Calcule e mostre sua área
(base * altura) e seu perímetro (soma dos 4 lados).
"""

base = int(input())
altura = int(input())

perimetro = (2*base) + (2*altura)
area = base*altura

print(f'Perímetro: {perimetro}\nÁrea: {area}')