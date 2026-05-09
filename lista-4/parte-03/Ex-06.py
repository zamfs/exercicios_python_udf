numeros = [2,5,3,1,8,7,11]

n_pesquisado = int(input('Digite um número para pesquisar na lista: '))

for index, numero in enumerate(numeros):
    if n_pesquisado == numero:
        print(f'Encontrado! número: {numero} index -> {index}')
        break
else:
    print('Número não encontrado na lista!')