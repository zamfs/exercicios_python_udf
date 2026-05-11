"""
Menu com validação
Escreva um programa que exiba o menu abaixo e solicite a escolha do usuário. Enquanto a opção for
inválida, o menu deve ser reexibido. Quando válida, exiba a opção escolhida.
[1] Cadastrar
[2] Consultar
[3] Sair
"""

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