limite = int(input())

fibonacci = 0
b = 1

while fibonacci <= limite:
    print(fibonacci)
    proximo = fibonacci + b
    fibonacci = b
    b = proximo