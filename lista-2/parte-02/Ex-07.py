"""
Verificação de senha. Defina uma senha fixa no código ("python123"). Leia a tentativa do usuário
e informe se o acesso foi permitido ou negado.
"""

senha = "python123"

entrada_usuario = input()

if entrada_usuario == senha:
    print('Acesso permitido!')
else:
    print('Acesso negado!')