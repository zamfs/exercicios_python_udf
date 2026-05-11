"""
Dados pessoais
Escreva uma função chamada ficha_cadastral que receba três parâmetros: nome (str), idade (int) e
altura (float). A função deve exibir os dados formatados, mostrando a altura com duas casas decimais.
No programa principal, leia os três dados e chame a função.
"""

def ficha_cadastral(nome_usuario, idade_usuario, altura_usuario):
    """
    Realiza a formatação de dados cadastrais.

    Parâmetros:
        nome_usuario (str)
        idade_usuario (int)
        altura_usuario (float)
    """
    print(f'\n================\nNome: {nome_usuario}\nIdade: {idade_usuario}\nAltura: {altura_usuario:.2f}\n================\n')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite a sua altura: '))

ficha_cadastral(nome,idade,altura)
