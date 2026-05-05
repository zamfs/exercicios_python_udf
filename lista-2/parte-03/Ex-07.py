mes = int(input('Digite o mês 1-12: '))

if mes >= 3 and mes <=5:
    print('Outono')
elif mes >=6 and mes <=8:
    print('Inverno')
elif mes >= 9 and mes <=11:
    print('Primavera')
else:
    print('Verão')