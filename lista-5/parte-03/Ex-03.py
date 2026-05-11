"""
Salário líquido
Escreva uma função chamada calcular_imposto que receba o salário bruto (float) e retorne o valor do
imposto conforme as faixas: até R$ 1.500,00 → isento (0.0); de R$ 1.500,01 a R$ 3.500,00 → 15%;
acima de R$ 3.500,00 → 27,5%. Em seguida, escreva uma função chamada salario_liquido que receba
o salário bruto, chame internamente calcular_imposto e retorne o salário líquido (bruto − imposto). No
programa principal, leia o nome (str) e o salário bruto do funcionário, chame salario_liquido e exiba
um contracheque formatado com nome, bruto, imposto e líquido.
"""

def calcular_imposto(salario_bruto):
    """
    Função para calcular a porcentagem de imposto levando em consideração o salário.

    Parâmetros:
        salario_bruto (float): valor do salário antes de ser descontado o imposto
    
    Retorno:
        O valor do imposto que será cobrado
    """

    if salario_bruto <= 1500.00:
        return 0.0
    elif salario_bruto <= 3500.00:
        return salario_bruto*(15/100)
    else:
        return salario_bruto*(27.5/100)

def salario_liquido(salario_bruto):
    """
    Função para calcular o valor final do salário, descontado o imposto.

    Parâmetros:
        salario_bruto (float): valor do salário antes de ser descontado o imposto
    
    Retorno:
        O valor final do salário
    """
    return salario_bruto - calcular_imposto(salario_bruto)

nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário para calcular o imposto: '))

imposto = calcular_imposto(salario)
salario_final = salario_liquido(salario)

print('=================================================')
print(f'Funcionário: {nome}\nSalário sem descontar imposto: {salario:.2f}\nImposto: {imposto:.2f}\nSalário final: {salario_final:.2f}')
print('=================================================')