"""
Par ou ímpar
Escreva uma função chamada verificar_paridade que receba um número inteiro (int) e exiba na tela se
ele é “par” ou “ímpar”. No programa principal, leia o número e chame a função.
"""

def verificar_paridade(numero):
    """
    Realizar a verificação de um número, se é par ou ímpar, e exibir na tela

    Parâmetros:
        numero (int)
    """
    if numero%2 == 0:
        print('Par')
    else:
        print('Ímpar')

num = int(input('Digite um número inteiro: '))
verificar_paridade(num)
