"""
Acesso seguro com .get()
Crie o dicionário config = {"tema": "escuro", "idioma": "pt-BR"}. Use .get() para acessar as chaves
"tema", "idioma" e "fonte" (que não existe), fornecendo "Arial" como valor padrão para a chave
inexistente.
"""

config = {
    "tema": "escuro",
    "idioma": "pt-BR"
}


print(config.get("tema", "Arial"))
print(config.get("idioma", "Arial"))
print(config.get("fonte", "Arial"))