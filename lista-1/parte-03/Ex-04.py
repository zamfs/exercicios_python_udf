nota  = float(input())
frequencia = int(input()) #porcentagem ex: 80%

verif_nota = nota >= 7.0
verif_frequencia = frequencia >= 75

aprovacao = verif_frequencia and verif_nota

print(f'A nota é maior ou igual a 7? {verif_nota}\nA frequencia é maior ou igual a 75? {verif_frequencia}\nAprovado? {aprovacao}')