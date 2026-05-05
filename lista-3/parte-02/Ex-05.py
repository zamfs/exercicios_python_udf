N = int(input())

soma = 0
num_impar = 1

while num_impar < N:
    soma += num_impar
    num_impar += 2

print(soma)