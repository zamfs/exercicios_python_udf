"""
Acesso a Parque de Diversões: Para entrar num brinquedo radical, a pessoa deve ter idade superior a 12 anos E altura de
pelo menos 1.50 metros. Leia os valores e exiba a permissão de acesso.
"""

idade = int(input())
verif_idade = idade > 12

altura = float(input())
verif_altura = altura >= 1.5

autorizacao = verif_altura and verif_idade

print(f'Autorizado à entrar no brinquedo: {autorizacao}')