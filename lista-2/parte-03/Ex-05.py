"""
Menu de lanchonete. Exiba um menu com 4 opções numeradas (lanche, suco, café, água) e
seus preços. Leia a opção e exiba o item escolhido com o valor. Se a opção for inválida, avise o
usuário.
"""

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