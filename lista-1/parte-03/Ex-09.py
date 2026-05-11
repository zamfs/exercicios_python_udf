"""
Voto Obrigatório: A lei determina que o voto é obrigatório para pessoas que possuam entre 18 e 69 anos (inclusive). Leia
a idade, valide os limites com a operação lógica E e exiba o resultado.
"""

idade = int(input())
maior_18 = idade >= 18
menor_69 = idade <= 69

voto_obrigatorio = maior_18 and menor_69

print(f'Voto obrigatório? {voto_obrigatorio}')