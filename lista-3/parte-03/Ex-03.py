idade = int(input('Digite a idade: '))

while idade < 0 or idade > 130:
    print('Idade inválida!')
    idade = int(input('Digite a idade novamente: '))

print('Idade aceita!')