"""
ogo de adivinhação
Escreva uma função chamada gerar_secreto que não receba parâmetros e retorne um número inteiro
aleatório entre 1 e 50 (use import random e random.randint). Escreva outra função chamada dar_dica
que receba o palpite (int) e o número secreto (int) e retorne a string “Maior”, “Menor” ou “Acertou”.
No programa principal, use gerar_secreto para obter o número, depois crie um laço while que peça
palpites ao usuário, chame dar_dica, exiba a dica e conte as tentativas. Ao acertar, exiba o total de
tentativas.
"""

import random

def gerar_secreto():
    """
    Função para gerar um número secreto entre 1 e 50

    Parâmetros:
        Não possui
    
    Retorno:
        Retorna o número secreto
    """
    return random.randint(1,50)

def dar_dica(palpite, numero_secreto):
    """
    Função que diz se o palpite está maior, menor ou se acertou o número secreto

    Parâmetros:
        palpite (int): número que o usuário usou na tentativa
        numero_secreto (int): número que foi sorteado na função gerar_secreto()
    
    Retorno:
        "Seu palpite é maior", se for maior que o numero_secreto
        "Seu palpite é menor", se for menor que o numero_secreto
        "Acertou", se o palpite for igual ao numero_secreto
    """

    if palpite > numero_secreto:
        return "Seu palpite é maior"
    elif palpite < numero_secreto:
        return "Seu palpite é menor"
    else:
        return "Acertou"

secreto = gerar_secreto()
tentativas = 1

while True:
    numero = int(input('Tente adivinhar o número secreto: '))

    print(dar_dica(numero, secreto))

    if dar_dica(numero, secreto) == "Acertou":
        print(f'Em {tentativas} tentativas')
        break
    else:
        tentativas += 1
