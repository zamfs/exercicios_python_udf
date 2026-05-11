"""
Formação de Grupos: Um professor quer dividir sua turma em grupos de 4 alunos. Leia o total de alunos na turma, calcule
e mostre quantos grupos completos serão formados (divisão inteira /) e quantos alunos ficarão de fora (resto da divisão %).
"""

numero_alunos = int(input())

numero_grupos = numero_alunos//4

sem_grupos = numero_alunos%4

print(f'Com grupos: {numero_grupos} grupos\nSem grupo: {sem_grupos} alunos')