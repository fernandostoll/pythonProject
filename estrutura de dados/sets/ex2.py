def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return {linha.strip() for linha in arquivo.readlines()}
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        return set()

# Nomes dos dois arquivos .txt
arquivo1 = 'arquivo1.txt'
arquivo2 = 'arquivo2.txt'

# Ler os CNPJs de ambos os arquivos
cnpjs_arquivo1 = ler_arquivo(arquivo1)
cnpjs_arquivo2 = ler_arquivo(arquivo2)

# Calcular quantos CNPJs precisam ser removidos para eliminar as duplicatas
cnpjs_repetidos = cnpjs_arquivo1.intersection(cnpjs_arquivo2)
total_repetidos = len(cnpjs_repetidos)

print(f"Quantidade de CNPJs a serem removidos: {total_repetidos}")