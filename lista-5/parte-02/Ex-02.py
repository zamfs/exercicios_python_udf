"""
Maior entre dois
Escreva uma função chamada maior que receba dois números inteiros (int) e retorne o maior deles. Se
forem iguais, retorne qualquer um. No programa principal, leia dois números, chame a função e exiba
o resultado.
"""

def maior_numero(a,b):
    """
    Realiza a comparação para descobrir qual é o maior número.

    Parâmetros:
        a (int): primeiro número
        b (int): segundo número
    
    Retorno:
        O maior número.
    """

    if a >= b:
        return a
    else:
        return b

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

print(f'O maior número é: {maior_numero(n1,n2)}')