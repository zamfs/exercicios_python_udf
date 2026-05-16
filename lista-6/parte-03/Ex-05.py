"""
Tupla como chave de dicionário
Crie um dicionário onde as chaves são tuplas (linha, coluna) e os valores são os conteúdos de uma
"planilha" 2x3. Exemplo: {(0,0): "Nome", (0,1): "Idade", ...}. Itere e exiba em formato tabular.
"""

tabela = {
    (0,0): "Nome",
    (0,1): "Idade",
    (0,2): "Curso",
    (1,0): "João",
    (1,1): "20",
    (1,2): "Engenharia"
}

cabecalho = ''
primeira_linha = ''

for coordenada, valor in tabela.items():
    if coordenada[0] == 0:
        cabecalho += '  ' + valor
    else:
        primeira_linha += '  ' + valor

print(cabecalho,'\n',primeira_linha)