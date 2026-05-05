idade = int(input())
maior_18 = idade >= 18
menor_69 = idade <= 69

voto_obrigatorio = maior_18 and menor_69

print(f'Voto obrigatório? {voto_obrigatorio}')