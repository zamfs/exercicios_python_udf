"""
Soma até valor sentinela
Escreva um programa que leia números inteiros até que o usuário digite 0 (sentinela). Ao final, exiba a
soma de todos os valores lidos (excluindo o sentinela).
"""

num = int(input('Quando quiser parar digite 0: '))
soma = 0

while num != 0:
    soma += num
    num = int(input())

print(soma)