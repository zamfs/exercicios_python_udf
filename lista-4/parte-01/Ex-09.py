"""
Crie um programa que exiba a seguinte sequência usando for e range():
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

#como é necessário 5 repetições e o no range é o valor -1 -> 6 - 1 = 5 repetições
MAX = 6
for i in range(1, MAX):
    NOVO_MAX = i + 1
    for j in range(1, NOVO_MAX):
        print(j, end=" ")
    print("\n")