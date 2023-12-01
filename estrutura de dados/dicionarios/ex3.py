import datetime

# calcular a idade com base no ano de nascimento
def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

# le informações do usuário
nome = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ctps = int(input("Digite o número da Carteira de Trabalho (0 se não tiver): "))

# para iniciar o dicionário com nome e idade
pessoa = {"Nome": nome, "Idade": calcular_idade(ano_nascimento)}

# Se tiver CTPS, ler informações adicionais
if ctps != 0:
    ano_contratacao = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o salário: "))

    # Calcular a idade de aposentadoria (considerando 35 anos de contribuição)
    idade_aposentadoria = calcular_idade(ano_contratacao) + 35

    # Adicionar informações adicionais ao dicionário
    pessoa["CTPS"] = ctps
    pessoa["Ano Contratação"] = ano_contratacao
    pessoa["Salário"] = salario
    pessoa["Idade de Aposentadoria"] = idade_aposentadoria

# dados finais
print("\nDados da Pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")