"""
Iterando com enumerate
Crie a lista tarefas = ["Estudar Python", "Fazer exercícios", "Revisar código", "Ler documentação"].
Use enumerate() com start=1 para exibir cada tarefa numerada.
"""
tarefas = ["Estudar Python", "Fazer exercícios", "Revisar código", "Ler documentação"]

for index, tarefa in enumerate(tarefas, start=1):
    print(f'{index}. {tarefa}')