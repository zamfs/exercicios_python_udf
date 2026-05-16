"""
Criando e acessando uma tupla
Crie uma tupla chamada coordenada com a latitude -15.79 e a longitude -47.88 (Brasília). Exiba cada
valor separadamente usando índices. Tente alterar a latitude para -22.90 e observe o erro.
"""

coordenada = (-15.79, -47.88)
print(f'Latitude: {coordenada[0]}\nLongitude: {coordenada[1]}')

# coordenada[0] = -22.90
#Erro porque um tupla não pode ser modificada
