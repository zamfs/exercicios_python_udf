"""
Validação de Triângulo: Para existir um triângulo, qualquer lado deve ser sempre menor que a soma dos outros dois. Leia
3 lados (A, B e C) e construa uma expressão (A < B+C E B < A+C E C < A+B) para exibir se formam um triângulo válido.
"""

a = int(input())
b = int(input())
c = int(input())

validacao_triagulo = (a< (b+c)) and (b< (a+c)) and (c< (b+a))

print(f'É um triângulo? {validacao_triagulo}')