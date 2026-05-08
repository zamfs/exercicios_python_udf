frase = input('Digite uma frase: ').lower()

vogais = 0
consoantes = 0
espacos = 0
outros_tipos_caracteres = 0


for digito in frase:
    if digito in 'aeiouãáéíóúõ':
        vogais += 1
    elif digito == ' ':
        espacos += 1
    elif digito in 'bcdfghjklmnpqrstvwxyzç':
        consoantes += 1
    else:
        outros_tipos_caracteres += 1
    
print(f'Vogais: {vogais}\nConsoantes: {consoantes}\nEspaços: {espacos}\nOutros tipos de caracter: {outros_tipos_caracteres}')