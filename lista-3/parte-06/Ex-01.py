valor = int(input())

nota200 = 0
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
resto = 0

while valor > 0:
    if (valor - 200) >= 0:
        nota200 += 1
        valor -= 200
    elif (valor - 100) >= 0:
        nota100 += 1
        valor -= 100
    elif (valor - 50) >= 0:
        nota50 += 1
        valor -= 50
    elif (valor - 20) >= 0:
        nota20 += 1
        valor -= 20
    elif (valor - 10) >= 0:
        nota10 += 1
        valor -= 10
    elif (valor - 5) >= 0:
        nota5 += 1
        valor -= 5
    elif (valor - 2) >= 0:
        nota2 += 1
        valor -= 2
    else:
        resto = valor
        valor -= resto

if resto == 0:
    print(f'Notas de 200: {nota200}\nNotas de 100: {nota100}\nNotas de 50: {nota50}\nNota de 20: {nota20}\nNota de 10: {nota10}\nNota de 5: {nota5}\nNota de 2: {nota2}')
else:
    print(f'Notas de 200: {nota200}\nNotas de 100: {nota100}\nNotas de 50: {nota50}\nNota de 20: {nota20}\nNota de 10: {nota10}\nNota de 5: {nota5}\nNota de 2: {nota2}\nResto: {resto}')