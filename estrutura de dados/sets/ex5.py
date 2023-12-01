def ler_votos_arquivo(arquivo):
    votos = set()
    with open(arquivo, 'r') as file:
        for linha in file:
            cpf = linha.strip()  # Remove espaços em branco e quebras de linha
            votos.add(cpf)
    return votos

# Ler os votos dos dois arquivos
votos_arquivo1 = ler_votos_arquivo("votos_arquivo1.txt")
votos_arquivo2 = ler_votos_arquivo("votos_arquivo2.txt")

# Combina os votos de ambos os arquivos
todos_os_votos = votos_arquivo1.union(votos_arquivo2)

# Crie um dicionário para contar os votos de cada candidato
contagem_de_votos = {}

# Suponha que você tenha uma lista de CPFs associados a candidatos
# Substitua esses CPFs pelos reais CPFs dos candidatos e seus nomes
candidato_a = set(["11111111111", "22222222222"])
candidato_b = set(["33333333333", "44444444444"])
candidato_c = set(["55555555555", "66666666666"])

# Contar votos para cada candidato
for cpf in todos_os_votos:
    if cpf in candidato_a:
        contagem_de_votos["Candidato A"] = contagem_de_votos.get("Candidato A", 0) + 1
    elif cpf in candidato_b:
        contagem_de_votos["Candidato B"] = contagem_de_votos.get("Candidato B", 0) + 1
    elif cpf in candidato_c:
        contagem_de_votos["Candidato C"] = contagem_de_votos.get("Candidato C", 0) + 1

# Imprimir a contagem de votos para cada candidato
for candidato, votos in contagem_de_votos.items():
    print(f"{candidato}: {votos} votos")