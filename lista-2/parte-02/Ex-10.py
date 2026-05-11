"""
Triângulo válido. Leia três valores representando lados de um triângulo. Informe se eles podem
ou não formar um triângulo (cada lado deve ser menor que a soma dos outros dois).
"""

a = int(input())
b = int(input())
c = int(input())

if (a<(b+c)) and (b<(a+c)) and (c<(b+a)):
    print('É um triângulo!')
else:
    print('Não é um triângulo')
