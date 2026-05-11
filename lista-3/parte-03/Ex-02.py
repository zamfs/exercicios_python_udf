"""
Senha de acesso
Escreva um programa que peça ao usuário uma senha numérica. O programa deve continuar pedindo
enquanto a senha digitada for diferente de 2025. Ao acertar, exiba "Acesso liberado" e quantas
tentativas foram necessárias.
"""

entrada = int(input('Digite a senha: '))

tentativas = 0

while entrada != 2025:
    print('Senha incorreta!')
    entrada = int(input('Digite a senha novamente: '))
    tentativas += 1

print('Acesso liberado!')