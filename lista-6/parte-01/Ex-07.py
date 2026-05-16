"""
Criando e acessando um dicionário
Crie um dicionário chamado aluno com as chaves "nome" (str), "idade" (int) e "curso" (str). Exiba cada
valor acessando pela chave. Altere a idade para 23 e exiba novamente.
"""

aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

print(f'Nome: {aluno["nome"]}\nIdade: {aluno["idade"]}\nCurso: {aluno["curso"]}')

aluno["idade"] = 23

print(f'\n\nNome: {aluno["nome"]}\nIdade: {aluno["idade"]}\nCurso: {aluno["curso"]}')