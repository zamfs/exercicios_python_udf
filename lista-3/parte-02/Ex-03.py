"""
 Maior e menor valor
Escreva um programa que leia uma sequência de números inteiros positivos até que o usuário digite 0.
Ao final, exiba o maior e o menor valor informado.
"""

print('Digite 0 para parar.')
num = int(input('Digite número: '))
maior = num
menor = num

while num != 0:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    num = int(input('Digite número: '))

print('Maior: ', maior, 'Menor: ', menor)
