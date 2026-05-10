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
