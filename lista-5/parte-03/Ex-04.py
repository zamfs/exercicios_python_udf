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
