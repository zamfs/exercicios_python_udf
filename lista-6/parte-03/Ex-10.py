"""
Relatório completo com todas as estruturas
Crie um programa que leia o nome, curso e 3 notas de 3 alunos. Armazene os dados em uma lista de
dicionários. Ao final, exiba: o boletim de cada aluno, a média geral da turma, os cursos únicos (usando
set) e um atupla com (melhor_media, pior_media).
"""

boletim_turma = []
boletim_aluno = {}

media_turma = 0
media_aluno = 0
melhor_media = 0
menor_media = float('inf') #colocando um valor inf, para quando houver a primeira verificação, a nota digitada ser menor

cursos = []

for _ in range(3):
    boletim_aluno['nome'] = input('Digite o nome: ')
    boletim_aluno['curso'] = input('Digite o curso: ')
    boletim_aluno['nota1'] = float(input('Digite a nota 1: '))
    boletim_aluno['nota2'] = float(input('Digite a nota 2: '))
    boletim_aluno['nota3'] = float(input('Digite a nota 3: ')
)
    media_aluno += (boletim_aluno['nota1'] + boletim_aluno['nota2'] + boletim_aluno['nota3'])/3

    cursos.append(boletim_aluno['curso'])

    if media_aluno > melhor_media:
        melhor_media = media_aluno
    if media_aluno < menor_media:
        menor_media = media_aluno

    boletim_turma.append(boletim_aluno)

media_turma = media_aluno / len(boletim_turma)

cursos = set(cursos)

maior_menor_media = (melhor_media, menor_media)

print('\n\nBOLETIM DOS ALUNOS')
for aluno in boletim_turma:
    print(f'\nAluno: {aluno['nome']}')
    print(f'Curso: {aluno['curso']}')
    print(f'Nota 1: {aluno['nota1']}\nNota 2: {aluno['nota2']}\nNota 3: {aluno['nota3']}')

print(f'\nMÉDIA GERAL DA TURMA: {media_turma:.2f}')

print(f'\nCURSOS: {cursos}')

print(f'\nMelhor média: {maior_menor_media[0]:.2f}\nMenor média: {maior_menor_media[1]:.2f}')