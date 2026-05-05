a = int(input())
b = int(input())
c = int(input())

validacao_triagulo = (a< (b+c)) and (b< (a+c)) and (c< (b+a))

print(f'É um triângulo? {validacao_triagulo}')