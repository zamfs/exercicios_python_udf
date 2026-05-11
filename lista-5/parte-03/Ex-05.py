"""
Relatório de notas
Escreva as seguintes funções: (a) ler_nota, que receba uma mensagem (str) como parâmetro e retorne
uma nota válida entre 0 e 10 (float), usando um laço while com try/except para validar a entrada; (b)
calcular_media, que receba três notas (float) e retorne a média aritmética; (c) classificar, que receba a
média (float) e retorne “Aprovado”, “Recuperação” ou “Reprovado” conforme as faixas ≥ 7, ≥ 5 ou <
5; (d) exibir_boletim, que receba nome (str), três notas e a situação (str) e exiba um boletim formatado.
No programa principal, leia o nome do aluno, use ler_nota três vezes, calcule a média com
calcular_media, classifique com classificar e exiba tudo com exibir_boletim.
"""

def ler_nota(msg):
    """
    Função para fazer a leitura da nota.

    Parâmetros:
        msg (str): mensagem que será exibida para o usuário.
    
    Retorno:
        Retorna uma nota
    """

    while True:
        try:
            nota = float(input(msg))

            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print('A nota precisa está entre 0 e 10!')
        except ValueError:
            print('ERRO: valor inválido!')

def calcular_media(nota_1, nota_2, nota_3):
    """
    Calcular a média aritmética das notas.

    Parâmetro:
        nota_1 (float): primeira nota
        nota_2 (float): segunda nota
        nota_3 (float): terceira nota
    
    Retorno:
        Retorna a média das notas
    """

    return (nota_1 + nota_2 + nota_3) / 3

def classificar(media):
    """
    Classifica o aluno de acordo com a média.

    Parâmetro:
        media (float): media das 3 notas do aluno
    
    Retorno:
        "Aprovado" - para médias >=7
        "Recuperação" - para médias >=5
        "Reprovado" - para médias >5
    """

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def exibir_boletim(nome_aluno, nota_1, nota_2, nota_3, media, situacao):
    """
    Função para gerar o boletim.

    Parâmetros:
        nome_aluno (str): nome do aluno
        nota_1 (float): primeira nota
        nota_2 (float): segunda nota
        nota_3 (float): terceira nota
        media (float): media das 3 notas do aluno
        situacao (str): aprovado, recuperação ou reprovado
    
    Retorno:
        Não possui, apenas exibe o boletim.
    """

    print(' - ========== - BOLETIM - ========== - ')
    print(f'\nAluno: {nome_aluno}')
    print(f'\nNota na prova 1: {nota_1:.2f}\nNota na prova 2: {nota_2:.2f}\nNota na prova 3: {nota_3:.2f}')
    print(f'\nMédia final: {media:.2f}')
    print(f'\nSITUAÇÃO: {situacao}\n')
    print(' - ================================= - ')

nome = input('Digite o nome do aluno: ')
n1 = ler_nota('Nota 1: ')
n2 = ler_nota('Nota 2: ')
n3 = ler_nota('Nota 3: ')
calculo_media = calcular_media(n1, n2, n3)
classificacao = classificar(calculo_media)
exibir_boletim(nome, n1, n2, n3, calculo_media, classificacao)