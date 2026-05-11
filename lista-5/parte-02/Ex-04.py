"""
Preço com desconto
Escreva uma função chamada aplicar_desconto que receba o preço original (float) e o percentual de
desconto (float, com valor padrão de 10.0). A função deve retornar o preço final. No programa
principal, leia o preço, chame a função uma vez sem informar o desconto (usará 10%) e outra vez
informando 25%, exibindo ambos os resultados.
"""

def aplicar_desconto(preco, percentual_desconto):
    """
    Função que pega o preço do produto e aplica o desconto.

    Parâmetros:
        preco (float): preço do produto
        percentual_desconto (int): porcentagem do valor do desconto - padrão 10%
    """
    desconto = 100 - percentual_desconto
    valor_final = preco*(desconto/100)

    return valor_final

preco_produto = float(input('Digite o valor do produto: '))

print(f'Valor final: {aplicar_desconto(preco_produto, 10):.2f}')
print(f'Valor com 25% de desconto: {aplicar_desconto(preco_produto, 25):.2f}')
