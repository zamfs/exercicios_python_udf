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
