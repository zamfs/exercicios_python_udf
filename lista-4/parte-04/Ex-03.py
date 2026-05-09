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