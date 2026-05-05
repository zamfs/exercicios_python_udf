capital = float(input())
taxa = float(input())
tempo = float(input()) #meses

capital_final = (capital*taxa*tempo) + capital

print(f'Juros rendidos: R${capital_final-capital}\nRendimento final: R${capital_final}')