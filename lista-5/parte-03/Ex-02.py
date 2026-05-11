"""
Calculadora modular
Escreva quatro funções: somar, subtrair, multiplicar e dividir. Cada uma recebe dois números (float) e
retorna o resultado da operação correspondente. A função dividir deve retornar a string “Erro: divisão
por zero” caso o divisor seja 0. No programa principal, leia dois números e um operador (+, -, *, /), use
uma estrutura if/elif para chamar a função adequada e exiba o resultado.
"""

def somar(a,b):
    """
    Função que realiza a soma entre dois números.

    Parâmetros:
        a (float): primeiro número
        b (float): segundo número
    
    Retorno:
        Retorna o resultado da soma.
    """
    return round(a+b,2)

def subtrair(a,b):
    """
    Função que realiza a subtração entre dois números.

    Parâmetros:
        a (float): primeiro número
        b (float): segundo número
    
    Retorno:
        Retorna o resultado da subtração.
    """
    return round(a-b,2)

def multiplicar(a,b):
    """
    Função que realiza a multiplicação entre dois números.

    Parâmetros:
        a (float): primeiro número
        b (float): segundo número
    
    Retorno:
        Retorna o resultado da multiplicação.
    """
    return round(a*b,2)

def dividir(a,b):
    """
    Função que realiza a divisão entre dois números.

    Parâmetros:
        a (float): dividendo
        b (float): divisor, diferente de 0
    
    Retorno:
        Retorna o resultado da divisão.
    """
    if b != 0:
        return round(a/b,2)
    else:
        return "Erro: divisão por zero"

operador = input("Digite a operação (+, -, *, /): ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = None

if operador == '+':
    resultado = somar(n1,n2)
elif operador == '-':
    resultado = subtrair(n1,n2)
elif operador == '*':
    resultado = multiplicar(n1,n2)
elif operador == '/':
    resultado = dividir(n1,n2)
else:
    print('Erro: operador não identificado!')

if resultado:
    print(f'{n1:.2f} {operador} {n2:.2f} = {resultado}')