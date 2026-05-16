"""
Merge de dicionários
Crie dois dicionários: estoque_loja1 = {"mouse": 10, "teclado": 5, "monitor": 3} e estoque_loja2 =
{"teclado": 8, "fone": 12, "monitor": 2}. Crie um terceiro dicionário com o estoque total (somando
quantidades de produtos em comum).
"""

estoque_loja1 = {
    "mouse": 10, 
    "teclado": 5, 
    "monitor": 3
}

estoque_loja2 = {
    "teclado": 8, 
    "fone": 12, 
    "monitor": 2
}

estoques = [estoque_loja1, estoque_loja2]

estoque_total = {}

for estoque in estoques:
    for p, q in estoque.items():
        if p not in estoque_total:
            estoque_total[p] = q
        else:
            estoque_total[p] += q

print('\nEstoque total')
for p, q in estoque_total.items():
    print(f'{p}: {q}')
    