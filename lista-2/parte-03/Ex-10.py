a = int(input())
b = int(input())
c = int(input())

if (a<(b+c)) and (b<(a+c)) and (c<(b+a)):
    if a == b == c:
        print('Triângulo equilátero!')
    elif a != b != c:
        print('Triângulo escaleno!')
    else:
        print('Triângulo isósceles!')
else:
    print('Não é um triângulo!')
