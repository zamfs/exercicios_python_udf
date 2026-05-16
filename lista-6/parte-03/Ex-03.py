"""
Invertendo um dicionário
Dado o dicionário siglas = {"BR": "Brasil", "AR": "Argentina", "CL": "Chile"}, crie um novo
dicionário invertido onde os valores se tornam chaves e as chaves se tornam valores. Use dict
comprehension.
"""

siglas = {
    "BR": "Brasil",
    "AR": "Argentina",
    "CL": "Chile"
}

siglas_invertido = {v:k for k,v in siglas.items()}

print(siglas_invertido)