a = 0 #número atual da sequência
b = 1 #próximo número da sequência

termos = int(input('Quantos termos da sequência de fibonacci: '))

for _ in range(termos):
    print(a)
    a, b = b, a + b