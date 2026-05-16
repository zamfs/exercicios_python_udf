"""
Operações de conjunto: alunos em comum
Crie os conjuntos python = {"Ana", "Bruno", "Carla", "Daniel"} e java = {"Bruno", "Daniel", "Eva",
"Fábio"}. Exiba: quem cursa ambas, quem cursa só Python, quem cursa só Java e quem cursa pelo
menos uma.
"""

python = {"Ana", "Bruno", "Carla", "Daniel"}
java = {"Bruno", "Daniel", "Eva","Fábio"}

print(f'Quem cursa Python e Java: {", ".join(sorted(python & java))}')
print(f'Quem cursa só Python: {", ".join(sorted(python - java))}')
print(f'Quem cursa apenas Java: {", ".join(sorted(java - python))}')
print(f'Quem cursa pelo menos uma: {", ".join(sorted(python | java))}')
