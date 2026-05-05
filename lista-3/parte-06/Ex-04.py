#Número da população da cidade A e B
A = 80000
B = 200000

anos = 0

while A <= B and anos <= 500:
    anos += 1
    A = A*1.03
    B = B*1.015

if anos > 500:
    print('Ultrapassou 500 anos!')
else:
    print(f'A cidade A ultrapassou a cidade B em: {anos} anos.')