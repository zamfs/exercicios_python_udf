salario = float(input())
verif_salario = salario > 2500.00


nome_limpo = input().capitalize()
if nome_limpo == "False":
    nome_limpo = False
elif nome_limpo == "True":
    nome_limpo = True

aprovacao_emprestimo = nome_limpo and verif_salario

print(f'O empréstimo poderá ser realizado? {aprovacao_emprestimo}')