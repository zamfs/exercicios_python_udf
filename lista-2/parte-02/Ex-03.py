"""
Aprovado ou reprovado. Leia a nota de um aluno (0 a 10). Exiba "Aprovado" se a nota for ≥ 7
ou "Reprovado" caso contrário
"""

nota = int(input())

if nota >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')