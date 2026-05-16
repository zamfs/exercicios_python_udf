"""
Verificação de pertencimento com set
Crie um conjunto de palavras proibidas: proibidas = {"spam", "fraude", "golpe"}. Leia uma frase via
input(), divida em palavras com .split() e verifique se alguma palavra proibida aparece na frase.
"""

proibidas = {"spam", "fraude", "golpe"}

frase = input('Dgite uma frase: ')

print(frase)

for palavra in frase:
    if palavra in proibidas:
        print(f'Palavra proibida: {palavra}')