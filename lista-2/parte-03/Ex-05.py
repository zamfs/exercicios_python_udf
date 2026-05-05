opcao = input()

opcao = opcao.lower()

if opcao == 'lanche':
    print('Lanche -- R$4,00')
elif opcao == 'suco':
    print('Suco -- R$2,00')
elif opcao == 'café':
    print('Café -- R$2,00')
elif opcao == 'água':
    print('Água -- 1,00')
else:
    print('Opção inválida! ')