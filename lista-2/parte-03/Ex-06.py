operador = input('Operador: ')
num1 = float(input('Num 1: '))
num2 = float(input('Num 2: '))

if operador == '+':
    print(num1,' + ',num2, ' = ', num1+num2)
elif operador == '-':
    print(num1,' - ',num2, ' = ', num1-num2)
elif operador == '*':
    print(num1,' * ',num2, ' = ', num1*num2)
elif operador == '/':
    if num2 == 0:
        print('Indefinido!')
    else:
        print(num1,' / ',num2, ' = ', num1/num2)
else:
    print('Opção inválida!')