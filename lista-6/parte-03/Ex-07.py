"""
Sistema de votação
Crie um conjunto de candidatos válidos: {"Ana", "Bruno", "Carla"}. Simule uma votação: leia 5 votos
via input(). Use um dicionário para contar os votos válidos e um contador para votos nulos. Exiba o
resultado.
"""

candidatos_validos = {
    "Ana": 0,
    "Bruno": 0,
    "Carla": 0,
    "nulo": 0
}

print('Candidatos: Ana, Bruno Carla')
for i in range(5):
    voto = input('Digite o voto (ou nulo): ')
    if voto == "Ana":
        candidatos_validos[voto] += 1
    elif voto == "Bruno":
        candidatos_validos[voto] += 1
    elif voto == "Carla":
        candidatos_validos[voto] += 1
    elif voto == "nulo":
        candidatos_validos[voto] += 1
    else:
        print('Opção inválida!')
        continue

print('\nResultado')
for c, v in candidatos_validos.items():
    if c == 'nulo':
        print(f'Votos nulos: {v}')
    else:
        print(f'Candidato {c}: {v} votos')