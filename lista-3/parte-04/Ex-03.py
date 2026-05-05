num = int(input())

contagem_digitos = 0

continuar = True

while continuar == True:
    num = num // 10
    if num > 0:
        contagem_digitos += 1
    else:
        contagem_digitos += 1
        continuar = False

print(contagem_digitos)