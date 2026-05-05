num = int(input())

raiz_teste = 0
raiz = 0

while raiz_teste**2 < num:
    raiz_teste+=1

    if (raiz_teste**2) == num:
        raiz = raiz_teste
    elif (raiz_teste**2) > num:
        raiz = raiz_teste - 1

print(raiz)
