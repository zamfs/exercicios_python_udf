temperatura = float(input())

if temperatura >= 0 and temperatura < 1:
    print('Gelado')
elif temperatura <= 15:
    print('Frio')
elif temperatura <= 25:
    print('Agradável')
elif temperatura <= 35:
    print('Quente')
elif temperatura > 35:
    print('Muito quente')