base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))
resultado = 1

for _ in range(expoente):
    resultado *= base
    print(resultado)

print(f'Resultado: {resultado}')