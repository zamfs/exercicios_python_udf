"""
Área do retângulo
Escreva uma função chamada area_retangulo que receba a base (float) e a altura (float) como
parâmetros e retorne a área. No programa principal, leia os valores, chame a função, armazene o
resultado em uma variável e exiba-o com duas casas decimais.
"""

def area_retangulo(b, h):
    """
    Função para calcular a área de um retângulo.

    Parâmetros:
        b (float): base do retângulo
        h (float): altura do retângulo
    
    Retorno:
        O valor da área do retângulo
    """
    return b*h

base = float(input('Digite o valor da base do retângulo: '))
altura = float(input('Digite o valor da altura do retângulo: '))

area = area_retangulo(base,altura)

print(f'Área: {area:.2f}')