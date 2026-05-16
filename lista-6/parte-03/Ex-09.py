"""
Agenda telefônica completa
Crie um programa de agenda telefônica usando um dicionário (nome → telefone). Implemente um
menu com as opções: 1-Adicionar contato, 2-Buscar contato, 3-Remover contato, 4-Listar todos, 5-
Sair. Use while True com break.
"""

agenda_telefonica = {}

while True:
    print('\nMenu\n1-Adicionar contato \n2-Buscar contato \n3-Remover contato \n4-Listar todos \n5-Sair')

    try: 
        opcao = int(input('Escolha um opção: '))

        if opcao == 1:
            nome = input('\nNome do contato: ')
            telefone = input('Digite o telefone: ')

            agenda_telefonica[nome] = telefone
            print('Adicinado')
        
        elif opcao == 2:
            busca = input('Digite o nome do contato da busca: ')

            if busca not in agenda_telefonica:
                print('\nEsse contato não existe!')
            else:
                print(f'\n{busca} - telefone: {agenda_telefonica[busca]}')

        elif opcao == 3:
            deletar = input('\nDigite o nome do contato que deseja deletar: ')

            if deletar not in agenda_telefonica:
                print('\nContato não existe')
            else:
                del agenda_telefonica[deletar]
                print('Deletado')
        
        elif opcao == 4:
            if not agenda_telefonica:
                print('\nNão há contatos ainda!')
            else:
                for n, t in agenda_telefonica.items():
                    print(f'{n} - telefone: {t}')
        
        elif opcao == 5:
            print('\nSaindo...')
            break

        else:
            print('\nOpção inválida')
            continue

    except ValueError:
        print('\nOcorreu um erro! Tente novamente!')
        continue