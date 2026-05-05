num = int(input())

if num <= 1:
    print('O número precisa ser maior do que 1!')
elif num == 2:
    print('Número primo')
else:
    raiz = int(num**0.5)

    teste_primo = 2
    validacao = True
    while validacao == True and teste_primo <= raiz:
        if num % teste_primo == 0:
            validacao = False
        else:
            teste_primo += 1

    if validacao == True:
        print('Número primo')
    else:
        print('Não é primo')