divisor = 1
termo = 1/divisor
sinal = 1

soma = 0

while termo > 0.000001:
    termo = termo * sinal
    soma += termo

    divisor += 2
    sinal *= -1
    termo = 1/divisor

print(termo)