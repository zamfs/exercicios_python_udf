def situacao_aluno(nota_1, nota_2):
    """
    Verifica se o aluno foi aprovado ou não.

    Parâmetros:
        nota_1 (float): primeira nota
        nota_2 (float): segunda nota
    
    Retorno:
        Uma sting falando "Aprovado", "Recuperação" ou "Reprovado"
    """
    media = (nota_1 + nota_2) / 2

    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'O aluno {nome} está {situacao_aluno(nota1,nota2)}')