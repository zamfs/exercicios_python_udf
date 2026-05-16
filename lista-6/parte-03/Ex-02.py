"""
Dicionário de listas: notas por disciplina
Crie o dicionário notas = {"Python": [8.5, 9.0, 7.5], "Java": [6.0, 7.0, 5.5], "C++": [9.5, 10.0, 9.8]}.
Itere sobre ele e exiba o nome da disciplina e a média das notas.
"""
notas = {
    "Python": [8.5, 9.0, 7.5],
    "Java": [6.0, 7.0, 5.5],
    "C++": [9.5, 10.0, 9.8]
}

for disciplina, notas in notas.items():
    media = 0
    for nota in notas:
        media += nota
    media /= len(notas)

    print(f'Disciplina: {disciplina}\n Média: {media:.2f}\n')