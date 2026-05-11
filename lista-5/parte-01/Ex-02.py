"""
Dobro de um número
Escreva uma função chamada exibir_dobro que receba um número inteiro (int) como parâmetro e
exiba na tela o dobro desse número. No programa principal, leia um inteiro via input() e chame a
função.
"""

def exibir_dobro(numero):
    """
    Exibe o dobro de um número inteiro

    Parâmetros:
        numero (int)
    """
    print(2*numero)

n = int(input('Digite um número inteiro: '))
exibir_dobro(n)
