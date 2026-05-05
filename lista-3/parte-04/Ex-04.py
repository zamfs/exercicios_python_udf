num = int(input())

soma_digitos = 0

continuar = True

while continuar == True:
    if num//10 == 0:
        continuar = False
        
    digito = num %10
    num = num//10

    soma_digitos += digito


print(soma_digitos)