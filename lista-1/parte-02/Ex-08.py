"""
Troca de Valores: Escreva um algoritmo que leia dois valores numéricos para as variáveis A e B. Em seguida, troque os
valores entre elas utilizando uma variável auxiliar e mostre os valores finais.
"""

a = int(input())
b = int(input())

aux = a
a = b
b = aux

print(f'Valores trocados... a: {a}, b: {b}')