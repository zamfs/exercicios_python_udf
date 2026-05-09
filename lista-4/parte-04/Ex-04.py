numero_linhas = int(input('Números de linhas do triângulo de Pascal: '))

for linha in range(numero_linhas):
    espacos_em_branco = numero_linhas - linha
    exibicao_linha = ''

    for _ in range(espacos_em_branco):
        exibicao_linha += ' '


    n = linha
    for k in range(n+1):

        n_fatorial = 1
        for i in range(1, n+1):
            n_fatorial *= i

        k_fatorial = 1
        for i in range(1, k+1):
            k_fatorial *= i
        
        fatorial_da_diferenca = 1
        for i in range(1, (n-k)+1):
            fatorial_da_diferenca *= i

        digito = n_fatorial/(k_fatorial*fatorial_da_diferenca)


        exibicao_linha += str(int(digito)) + ' '
    
    print(exibicao_linha)
