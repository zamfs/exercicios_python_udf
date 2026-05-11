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