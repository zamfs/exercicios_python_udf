"""
Escreva um programa que percorra uma lista de nomes utilizando enumerate() e exiba cada nome com
seu número de ordem, começando em 1.
Exemplo de saída:
1. Ana
2. Bruno
3. Carla
"""

nomes = ["Ana","Bruno","Carla"]
 
for ordem,nome in enumerate(nomes, start= 1):
    print(f'{ordem}. {nome}')