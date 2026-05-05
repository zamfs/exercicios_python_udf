num = int(input())

repeticao = True

contando_digitos = num
num_digitos = 0

while repeticao == True:
    if contando_digitos//10 == 0:
        repeticao = False #ainda vai finalizar a última execução, mas não irá iniciar a próxima, pois será a última
    contando_digitos = contando_digitos//10
    num_digitos +=1

invertendo_num = num
repeticao = True

num_invertido = 0

divisor_digito = 10**(num_digitos-1)

multiplicador_num_invertido = 1

while repeticao == True:
    if invertendo_num//10 == 0:
        repeticao = False
    digito = invertendo_num//divisor_digito

    num_invertido += digito*multiplicador_num_invertido

    invertendo_num = invertendo_num - (digito*divisor_digito)

    divisor_digito = divisor_digito / 10
    multiplicador_num_invertido = multiplicador_num_invertido * 10

print('NÚMERO INVERTIDO: ', int(num_invertido))
