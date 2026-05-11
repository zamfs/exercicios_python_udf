"""
Faça um programa que leia n notas de alunos (valores de 0 a 10) e exiba ao final: a média da turma, a
maior nota e quantos alunos ficaram acima da média. Utilize um laço for com padrão acumulador e
uma lista para armazenar as notas.
"""

repeticao = int(input('Quantas notas de alunos serão lidas: '))

soma_notas = 0
maior_nota = 0
acima_media = 0

for _ in range(repeticao):
    nota = float(input('Digite a nota: '))

    soma_notas += nota

    if nota > maior_nota:
        maior_nota = nota
    
    if nota >= 7.00:
        acima_media += 1
    
media = soma_notas/repeticao

print(f'Média das notas: {media:.2f}\nMaior nota: {maior_nota:.2f}\nAprovados: {acima_media}')