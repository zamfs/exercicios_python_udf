"""
Saudação personalizada
Escreva uma função chamada saudacao que receba um nome (str) como parâmetro e exiba na tela a
mensagem “Olá, [nome]! Seja bem-vindo(a) ao Python.”. No programa principal, peça ao usuário que
digite seu nome e chame a função.
"""

def saudacao(nome_usuário):
    """
    Realizar a saudação

    Parâmetros:
        nome_usuario (str)
    """
    print(f'Olá, {nome_usuário}! Seja bem-vindo(a) ao Python.')

nome = input('Digite seu nome: ')
saudacao(nome)
