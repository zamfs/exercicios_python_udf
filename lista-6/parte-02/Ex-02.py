"""
Ordenação e estatísticas
Leia 5 notas (float) via input() e armazene em uma lista. Exiba a lista ordenada (crescente e
decrescente), a maior nota, a menor nota, a soma e a média.
"""

notas = []

for _ in range(5):
    nota = float(input('Digte a nota: '))
    notas.append(nota)

notas.sort()

print(f'\n\nNotas em ordem crescente: {notas}')
print(f'Notas em ordem decrescente: {notas[::-1]}')

print(f'\nMaior nota: {max(notas)}\nMenor nota: {min(notas)}')

print(f'\nSoma: {sum(notas):.2f}\nMédia: {(sum(notas)/ len(notas)):.2f}')