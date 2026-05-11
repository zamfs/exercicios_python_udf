"""
Estação do ano pelo mês. Leia o número do mês (1–12) e exiba a estação do ano aproximada
no hemisfério sul: Verão (dez–fev), Outono (mar–mai), Inverno (jun–ago), Primavera (set–nov).
"""

mes = int(input('Digite o mês 1-12: '))

if mes >= 3 and mes <=5:
    print('Outono')
elif mes >=6 and mes <=8:
    print('Inverno')
elif mes >= 9 and mes <=11:
    print('Primavera')
else:
    print('Verão')