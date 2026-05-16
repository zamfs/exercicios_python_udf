"""
Adicionando e removendo de dicionário
Crie o dicionário produto = {"nome": "Notebook", "preço": 3500.00}. Adicione a chave "estoque" com
valor 10. Remova a chave "preço" com del. Exiba o dicionário final.
"""

produto = {
    "nome": "Notebook",
    "preço": 3500.00
}

print(produto)

produto["estoque"] = 10

del produto["preço"]

print(produto)