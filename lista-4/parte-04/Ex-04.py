"""
Escreva um programa que gere e exiba o Triângulo de Pascal com n linhas (informado pelo usuário).
Utilize laços for aninhados. Cada linha deve ser exibida formatada e centralizada. Utilize pass como
placeholder se decidir separar a lógica de cálculo da lógica de exibição em etapas distintas.
Exemplo para n=5:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

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
