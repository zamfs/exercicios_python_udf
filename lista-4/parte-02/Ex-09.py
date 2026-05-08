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