"""
Fatorial
Escreva uma função chamada fatorial que receba um número inteiro não negativo (int) e retorne o
valor de n! (n fatorial). Use um laço while dentro da função para calcular o resultado. No programa
principal, leia o número, chame a função e exiba o resultado no formato “5! = 120”.
"""

def fatorial(numero):
    """
    Calcula o fatorial de um número.

    Parâmetros:
        numero (int): número inteiro não negativo
    
    Retorno:
        O valor do fatorial do número
    """
    valor_fatorial = 1
    while numero >= 1:
        valor_fatorial *= numero
        numero -= 1
    
    return valor_fatorial

n = int(input('Digite um número inteiro positivo para calcular o fatorial: '))
print(f'{n}! = {fatorial(n)}')
