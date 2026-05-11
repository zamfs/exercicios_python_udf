"""
Validador de triângulo
Escreva uma função chamada eh_triangulo que receba três lados (float) e retorne True se eles formam
um triângulo válido (cada lado deve ser menor que a soma dos outros dois) ou False caso contrário.
Em seguida, escreva uma segunda função chamada tipo_triangulo que receba os mesmos três lados e
retorne “Equilátero”, “Isósceles” ou “Escaleno”. No programa principal, leia os três lados, use
eh_triangulo para verificar a validade e, se válido, chame tipo_triangulo e exiba a classificação.
"""

def eh_triangulo(lado_1,lado_2,lado_3):
    """
    Função para verificar se os 3 lados formam um triângulo

    Parâmetros:
        lado_1 (float): primeiro lado do triângulo
        lado_2 (float): segundo lado do triângulo
        lado_3 (float): terceiro lado do triângulo
    
    Retorno:
        True se for triângulo
        False se não for triângulo
    """
    if lado_1 < lado_2+lado_3 and lado_2 < lado_1+lado_3 and lado_3 < lado_1+lado_2:
        return True
    else: return False

def tipo_triângulo(lado_1,lado_2,lado_3):
    """
    Realiza a classificação do tipo de triângulo (Isósceles, Equilátero ou Escaleno).

    Parâmetros:
        lado_1 (float): primeiro lado do triângulo
        lado_2 (float): segundo lado do triângulo
        lado_3 (float): terceiro lado do triângulo
    
    Retorno
        "Equilátero" para todos os lados iguais
        "Isósceles" para apenas dois lados iguais
        "Escaleno" para todos os lados diferentes
    """
    if lado_1 == lado_2 == lado_3:
        return "Equilátero"
    elif lado_1 != lado_2 != lado_3:
        return "Escaleno"
    else:
        return "Isósceles"
    
l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

validacao = eh_triangulo(l1,l2,l3)

if validacao:
    print(f'Classificação: {tipo_triângulo(l1,l2,l3)}.')

else:
    print('Não é triângulo!')