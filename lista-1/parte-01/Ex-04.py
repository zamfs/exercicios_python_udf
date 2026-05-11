"""
Média de Três Notas: Escreva um algoritmo que leia três notas de um aluno, calcule e exiba a média aritmética simples
entre elas.
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1+n2+n3)/3

print(f'Média: {round(media,2)}')