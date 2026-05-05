capital_inicial = float(input('Digite o capital inicial: '))
taxa_juros = float(input('Digite a taxa de juros mensais. (Exemplo de entrada: 1.5): '))
valor_desejado = float(input('Valor desejado: '))
meses = 0
capital = 0

while capital < valor_desejado:
    meses += 1
    capital = capital_inicial * ((1 + (taxa_juros/100))**meses)


print(f'Capital inicial: {capital_inicial:.2f}. Capital final: {capital:.2f}')
print(f'Tempo necessário para conseguir esse valor: {meses} meses')
