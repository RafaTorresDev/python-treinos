# EXERCICIO ACADEMIA
# Pratique: and | or | not | in | not in

# Crie um sistema que verifique se uma pessoa pode entrar.

# Regras:
# - Ter 18 anos ou mais
# - Modalidade deve ser permitida
# - Modalidade não pode estar bloqueada

# Use:
# idade = ?
# modalidade = ?
# permitidas = ["musculação", "boxe", "natação"]
# bloqueadas = ["boxe", "crossfit"]

# Resultado:
# "Acesso permitido!" ou "Acesso negado!"

idade = int(input("Digite a sua idade: "))
modalidade = input("Qual a sua modalidade: ")
permitidas = ["musculaçao", "nataçao"]
nao_permitidas = ["boxe", "crossfit"]

if idade >= 18 and modalidade in permitidas and modalidade not in nao_permitidas:
    print("Acesso permitido!")
else:
    print("Acesso negado!")