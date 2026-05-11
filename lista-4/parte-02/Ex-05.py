"""
Faça um programa que calcule a potência de um número sem usar o operador **. O programa deve ler
a base e o expoente do usuário, e utilizar um laço for para realizar multiplicações sucessivas.
Exemplo: base=3, expoente=4 → 3 × 3 × 3 × 3 = 81
"""

base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))
resultado = 1

for _ in range(expoente):
    resultado *= base
    print(resultado)

print(f'Resultado: {resultado}')