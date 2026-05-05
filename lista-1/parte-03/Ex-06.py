idade = int(input())
verif_idade = idade > 12

altura = float(input())
verif_altura = altura >= 1.5

autorizacao = verif_altura and verif_idade

print(f'Autorizado à entrar no brinquedo: {autorizacao}')