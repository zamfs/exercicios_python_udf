"""
Média com contagem automática
Escreva um programa que leia notas de alunos (entre 0 e 10) até que seja digitado um valor negativo
(sentinela). Ao final, exiba a quantidade de notas lidas e a média aritmética.
"""

print('Quando quiser parar digite uma nota negativa.')
nota = float(input())

contagem_notas = 0
soma_notas = 0

while nota >= 0:
    contagem_notas+=1
    soma_notas+=nota
    nota=float(input())

media = soma_notas/contagem_notas

print('Média -> ', media)