print('Quando quiser parar digite uma nota negativa.')
nota = float(input())

contagem_notas = 0
soma_notas = 0

while nota >= 0:
    contagem_notas+=1
    soma_notas+=nota
    nota=float(input())

media = soma_notas/contagem_notas

print('Média -> ', media)