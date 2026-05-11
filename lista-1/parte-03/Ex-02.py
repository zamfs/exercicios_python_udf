"""
Saldo Bancário Positivo: Leia o saldo de uma conta corrente. Atribua a uma variável lógica e exiba se a conta está
estritamente positiva (maior que zero).
"""

saldo_bancario = int(input())

saldo_positivo = saldo_bancario > 0 #estritamente maior do que 0

print(f'O saldo está postivo? {saldo_positivo}')