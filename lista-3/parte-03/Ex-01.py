"""
Entrada válida (intervalo)
Escreva um programa que solicite ao usuário um número entre 1 e 100, repetindo a solicitação
enquanto o valor informado estiver fora desse intervalo. Ao receber um valor válido, exiba-o.
"""

num = int(input('Digite um número entre 1 e 100: '))

while num < 1 or num > 100:
    print('Número inválido!')
    num = int(input('Digite um número entre 1 e 100: '))
print('Número válido!')