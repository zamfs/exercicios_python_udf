print('[1]Cadastrar [2]Consultar [3]Sair')
opcao = int(input('Escolha uma opção: '))

while opcao < 1 or opcao > 3:
    print('Opção inválida!')
    opcao = int(input('Escolha uma opção válida: '))

if opcao == 1:
    print('Cadastrar')
elif opcao == 2:
    print('Consultar')
else:
    print('Sair')