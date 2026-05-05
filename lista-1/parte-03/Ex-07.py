idade = int(input())
verif_idade = idade > 65

desempregado = input().capitalize()
if desempregado == "False":
    desempregado = False
elif desempregado == "True":
    desempregado = True


isencao = desempregado or verif_idade

print(f'O candidato terá a isenção? {isencao}')