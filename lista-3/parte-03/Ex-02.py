entrada = int(input('Digite a senha: '))

tentativas = 0

while entrada != 2025:
    print('Senha incorreta!')
    entrada = int(input('Digite a senha novamente: '))
    tentativas += 1

print('Acesso liberado!')