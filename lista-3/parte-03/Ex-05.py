num1 = int(input('Digite o primeiro número para divisão: '))
num2 = int(input('Digite o segundo número para divisão (não pode ser 0): '))

while num2 == 0:
    print('O segundo número não pode ser o 0!')
    num2 = int(input('Digite ele novamente: '))

divisao = num1 / num2
print('Resultado: ',divisao)