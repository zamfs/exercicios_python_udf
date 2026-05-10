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
