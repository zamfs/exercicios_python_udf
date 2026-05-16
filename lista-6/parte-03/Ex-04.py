"""
 Filtrando lista de dicionários
Dada a lista produtos = [{"nome": "Mouse", "preço": 50}, {"nome": "Teclado", "preço": 120},
{"nome": "Monitor", "preço": 900}, {"nome": "Fone", "preço": 80}], use list comprehension para criar
uma nova lista contendo apenas os produtos com preço acima de 100.
"""

produtos = [
    {
    "nome": "Mouse",
    "preço": 50
    },
    {
    "nome": "Teclado",
    "preço": 120
    },
    {
    "nome": "Monitor",
    "preço": 900
    }, 
    {
    "nome": "Fone",
    "preço": 80
    }
]

produtos_acima_100 = [produto for produto in produtos if produto["preço"] > 100]

print(produtos_acima_100)