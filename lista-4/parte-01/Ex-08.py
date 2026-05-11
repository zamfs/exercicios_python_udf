"""
Escreva um programa que leia 5 números do usuário e, ao final, exiba a soma e a média aritmética
desses números. Use o padrão acumulador com for.
"""

soma = 0 
for i in range(5):
    valor = int(input('Digite um número: '))
    soma += valor

print(soma)