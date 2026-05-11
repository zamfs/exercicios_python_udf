"""
Divisão de Conta de Pizzaria: Leia o valor total de uma conta e a quantidade de amigos na mesa. Calcule e exiba quanto
cada um deverá pagar.
"""

valor_conta = float(input())
pessoas_a_pagar = int(input())

valor_dividido = valor_conta/pessoas_a_pagar

print(f'O valor para cada um será: R${valor_dividido}')