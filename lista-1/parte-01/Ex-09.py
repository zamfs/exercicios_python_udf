"""
Conversão de Moeda: Leia um valor financeiro em Reais (R$) e a cotação atual do Dólar (US$). Calcule e mostre a quantia
equivalente em dólares.
"""

reais = float(input())
cotacaoUSD = float(input())

valorUSD = reais / cotacaoUSD

print(f'O valor em dolares é: {round(valorUSD, 2)} USD')