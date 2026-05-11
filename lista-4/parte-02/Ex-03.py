"""
Crie um programa que calcule a soma dos 50 primeiros termos da série: 1 + 1/2 + 1/3 + 1/4 + ... + 1/50
(série harmônica).
"""

soma = 0
for i in range(1,51):
    soma += 1/i

print(soma)