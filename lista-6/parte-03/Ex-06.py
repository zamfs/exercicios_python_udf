"""
Análise de texto com múltiplas estruturas
Leia uma frase via input(). Usando as estruturas adequadas, exiba: o número total de palavras (lista), as
palavras únicas (conjunto), a frequência de cada palavra (dicionário) e a palavra mais frequente.
"""

texto = input('Digite um texto: ')

total_palavras = texto.split()
frequencia_palavra = {}


for palavra in total_palavras:
    if palavra not in frequencia_palavra:
        frequencia_palavra[palavra] = 1
    else:
        frequencia_palavra[palavra] += 1

palavras_unicas = set(total_palavras)

print(f'Total de palavras: {len(total_palavras)}. Conjunto das palavras: {palavras_unicas}')
for p, f in frequencia_palavra.items():
    print(f'{p}: {f}')

comparador_mais_frequente = 0
palavra_mais_frequente = ''
for p, f in frequencia_palavra.items():
    if f > comparador_mais_frequente:
        mais_frequente = f
        palavra_mais_frequente = p
print(f'Palavra mais frequente: {palavra_mais_frequente}')