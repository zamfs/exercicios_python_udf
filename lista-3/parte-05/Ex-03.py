e = 1 #começa com 1, pois o valor de 1/0! é 1
contador = 0
soma = 0
i = 1
fatorial = 1

while e > 0.0001:
    soma += e

    fatorial *= i
    i+=1

    e = (1/fatorial)
    
    contador+=1

print(soma)
print(contador)
