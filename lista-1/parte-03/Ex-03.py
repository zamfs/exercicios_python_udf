"""
Verificação de Número Par: Leia um número inteiro. Utilize o operador de resto da divisão por 2 e o operador de igualdade
para verificar e exibir se o número é par.
"""

num = int(input())

par = ((num%2) == 0)

print(f'O número é par? {par}')