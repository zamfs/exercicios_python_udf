n = int(input('Digite um número: '))

if n <= 1:
    print('Não é primo')
else:
    raiz = 2
    check = False
    while check == False:
        if raiz*raiz == n:
            check = True
        elif raiz*raiz > n:
            raiz -= 1
            check = True
        else:
            raiz += 1

    primo = True
    for divisor in range(2, raiz+1):
        if n % divisor == 0:
            primo = False
    
    if primo == True:
        print('É primo!')
    else:
        print('Não é primo')        