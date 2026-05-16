"""
Adicionando e removendo elementos
Crie a lista compras = ["pão", "leite"]. Adicione "ovos" ao final com append(). Insira "manteiga" na
posição 1 com insert(). Remova "leite" com remove(). Exiba a lista após cada operação.
"""

compras = ["pão", "leite"]
print(f'Lista de compras inicial: {compras}')

compras.append("ovos")
print(f'Item adicionado: {compras}')

compras.insert(1, "manteiga")
print(f'Item adicionado: {compras}')

compras.remove("leite")
print(f'Item removido: {compras}')