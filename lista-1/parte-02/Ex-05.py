"""
Cálculo de Salário Líquido: Leia o salário bruto de um profissional e calcule o desconto de 8% referente ao INSS. Exiba o
valor do desconto e o salário líquido restante.
"""

salario_anterior = float(input())

salario_com_desconto = salario_anterior * 0.92

print(f'Desconto do INSS: R${salario_anterior-salario_com_desconto}\nNovo salário: R${salario_com_desconto}')