"""
Escreva um programa que simule um sistema de cadastro simplificado. O programa deve:
a) Usar while True para manter o menu ativo;
b) Oferecer opções: 1 – Adicionar nome, 2 – Listar nomes, 3 – Buscar nome, 4 – Sair;
c) Na opção 1, adicionar o nome a uma lista;
d) Na opção 2, usar for com enumerate() para listar os nomes;
e) Na opção 3, usar for-else com break para buscar;
f) Na opção 4, usar break para encerrar;
g) Para opções inválidas, usar continue
"""

print('==== MENU ====')
print('1 - Cadastrar\n2 - Consultar\n3 - Relatório\n4 - Sair')

lista_nomes = []

while True:
    try:
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome: ')
            lista_nomes.append(nome)
        elif opcao == 2:
            print('---- LISTA NOMES ----')
            for index, nome in enumerate(lista_nomes):
                print('* ', nome)
        elif opcao == 3:
            nome_busca = input('Digite o nome para busca: ')
            for nome in lista_nomes:
                if nome == nome_busca:
                    print('Econtrado!')
                    break
            else:
                print('Nome não encontrado na lista!')
        elif opcao == 4:
            print('Encerrando...')
            break
        else:
            print('Opção não existente...')
            continue


    except ValueError:
        print('Entrada inválida: ')
        continue