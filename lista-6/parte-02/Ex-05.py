"""
Desempacotamento de tuplas
Crie uma lista de tuplas representando alunos: [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]. Use um
for com desempacotamento para exibir o nome e a nota de cada aluno, indicando se foi aprovado (nota
>= 7).
"""

alunos = [("Ana", 8.5), ("Bruno", 6.0), ("Carla", 9.2)]

for nome, nota in alunos:
    if nota >= 7:
        print(f'\nAluno: {nome}\nSituação: APROVADO com a nota {nota}')
    else:
        print(f'\nAluno: {nome}\nSituação: REPROVADO com a nota {nota}')
