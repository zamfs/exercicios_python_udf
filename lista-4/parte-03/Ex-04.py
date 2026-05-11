"""
Crie o esqueleto de um programa de menu com 4 opções (1 – Cadastrar, 2 – Consultar, 3 – Relatório, 4
– Sair). Utilize pass como placeholder nas opções 1, 2 e 3 (ainda não implementadas), e break na
opção 4 para encerrar o laço.
"""

print('==== MENU ====')
print('1 - Cadastrar\n2 - Consultar\n3 - Relatório\n4 - Sair')

while True:
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1 or opcao == 2 or opcao == 3:
        pass
    else:
        break