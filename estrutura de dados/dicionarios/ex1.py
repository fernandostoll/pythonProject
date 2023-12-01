# Função para determinar a situação com base na média
def determinar_situacao(media):
    if media >= 7.0:
        return "APROVADO"
    elif media >= 5.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

# Solicitar nome e média do aluno
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

# Calcula a situação usando a função determinar_situacao
situacao = determinar_situacao(media)

# dados do aluno
aluno = {
    "Nome": nome,
    "Nota": media,
    "Situação": situacao
}

# Mostrar os dados do aluno
print("\nDados do Aluno:")
for chave, valor in aluno.items():
    print(f"{chave} - {valor}")