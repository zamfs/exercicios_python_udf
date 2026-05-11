"""
Conversão de temperatura
Escreva uma função chamada celsius_para_fahrenheit que receba uma temperatura em graus Celsius
(float) e exiba na tela o valor convertido para Fahrenheit, usando a fórmula F = C × 9/5 + 32. No
programa principal, leia a temperatura e chame a função.
"""

def celsius_para_fahrenheit(temperatura_celsius):
    """
    Realiza a conversão de Celsius para Fahrenheit e exibe na tela

    Parâmetros:
        temperatura_celsius (float): em Celsius
    """

    fahrenheit = (temperatura_celsius*9/5) + 32

    print(f'{fahrenheit}°F')

temperatura = float(input('Digite a temperatura em Celsius: '))
celsius_para_fahrenheit(temperatura)