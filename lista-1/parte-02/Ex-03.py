"""
Reajuste Salarial: Faça um algoritmo que leia o salário atual de um funcionário e aplique um aumento de 15%. Exiba o
valor do aumento numérico e o novo salário
"""

salario_anterior = float(input())

salario_com_aumento = salario_anterior * 1.15

print(f'O valor do aumento: R${salario_com_aumento-salario_anterior}\nNovo salário: R${salario_com_aumento}')