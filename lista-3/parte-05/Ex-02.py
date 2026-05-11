"""
Cálculo de raiz inteira
Escreva um programa que leia um número inteiro positivo N e determine a sua raiz quadrada inteira,
ou seja, o maior inteiro R tal que R² ≤ N. Não utilize funções prontas de raiz.
"""

num = int(input())

raiz_teste = 0
raiz = 0

while raiz_teste**2 < num:
    raiz_teste+=1

    if (raiz_teste**2) == num:
        raiz = raiz_teste
    elif (raiz_teste**2) > num:
        raiz = raiz_teste - 1

print(raiz)
