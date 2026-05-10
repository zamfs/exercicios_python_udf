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