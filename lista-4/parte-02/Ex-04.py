palavras = ["Python", "Programação"]

for palavra in palavras:
    for index, letra in enumerate(palavra, start=1):
        if index == len(palavra):
            print(f'{palavra} ({index} letras)')