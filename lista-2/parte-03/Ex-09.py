jogador1 = input().lower()
jogador2 = input().lower()

if jogador1 == 'pedra' and jogador2 == 'tesoura':
    print('Jogador 1 vencedor!')
elif jogador1 == 'pedra' and jogador2 == 'papel':
    print('Jogador 2 vencedor!')
elif jogador1 == 'papel' and jogador2 == 'tesoura':
    print('Jogador 2 vencedor!')
elif jogador1 == 'papel' and jogador2 == 'pedra':
    print('Jogador 1 vencedor!')
elif jogador1 == 'tesoura' and jogador2 == 'papel':
    print('Jogador 1 vencedor!')
elif jogador1 == 'tesoura' and jogador2 == 'pedra':
    print('Jogador 2 vencedor!')
else:
    print('Empate!')