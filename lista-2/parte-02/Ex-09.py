"""
Troco ou valor insuficiente. Leia o preço de um produto e o valor pago. Se o pagamento for
suficiente, exiba o troco; caso contrário, informe quanto falta.
"""

preco_produto = float(input())
pagamento = float(input())

if pagamento > preco_produto:
    print(f'Pagamento feito com sucesso! Troco: R$ {pagamento-preco_produto}')
else:
    print(f'Dinheiro insuficiente! Falta: R$ {preco_produto-pagamento}')