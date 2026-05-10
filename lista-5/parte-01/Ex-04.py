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