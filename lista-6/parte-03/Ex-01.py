"""
Lista de dicionários: cadastro de alunos
Leia o nome e duas notas de 3 alunos. Armazene cada aluno como um dicionário com chaves "nome",
"nota1", "nota2" e "media". Adicione cada dicionário a uma lista. Ao final, exiba o boletim completo
"""

lista_notas = []

for _ in range(3):
    aluno = {}

    aluno["nome"] = input('Digite o nome do aluno: ')
    aluno["nota1"] = float(input('Digite a nota 1: '))
    aluno["nota2"] = float(input('Digite a nota 2: '))

    lista_notas.append(aluno)

print('\n===========BOLETIM===========')
for aluno in lista_notas:
    print(f'Nome: {aluno["nome"]}')
    print(f'Nota 1: {aluno["nota1"]}')
    print(f'Nota 2: {aluno["nota2"]}\n\n')
    