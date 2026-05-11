"""
Validação de idade
Escreva um programa que leia a idade de uma pessoa, aceitando apenas valores entre 0 e 130.
Enquanto o valor for inválido, o programa deve exibir uma mensagem de erro e solicitar nova entrada.
"""

idade = int(input('Digite a idade: '))

while idade < 0 or idade > 130:
    print('Idade inválida!')
    idade = int(input('Digite a idade novamente: '))

print('Idade aceita!')