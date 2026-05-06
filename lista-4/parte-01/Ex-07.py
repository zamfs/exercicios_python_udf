n = int(input('Digite um número: '))
fatorial = 1

for num in range(n,0,-1):
    fatorial *= num

print(fatorial)