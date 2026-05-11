"""
Crie um programa que exiba todos os números primos entre 2 e 100. Para cada número do intervalo,
use um laço for interno com break para testar divisibilidade, e a estrutura for-else para identificar os
primos.
"""

for n in range(2,101):
    raiz = 1
    for i in range(n):
        if i*i == n:
            raiz = i
            break
        elif i*i > n:
            raiz = i-1
            break
        else:
            continue

    for i in range(2,raiz+1):
        if n % i == 0:
            break
    else:
        print(n)