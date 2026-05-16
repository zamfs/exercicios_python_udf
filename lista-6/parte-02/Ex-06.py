"""
Iterando em dicionário com .items()
Crie o dicionário capitais = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "Chile": "Santiago",
"Peru": "Lima"}. Itere com .items() e exiba "A capital de [país] é [capital].".
"""

capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima"
}

for pais, capital in capitais.items():
    print(f'A capital do(a) {pais} é {capital}')