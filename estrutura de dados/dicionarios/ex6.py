#funçao de bytes para megabytes
def bytes_para_megabytes(bytes):
    return bytes / (1024 * 1024)

#funçao calcular percentual de uso
def calcular_percentual(espaco, total):
    return (espaco / total) * 100

#inicia variavel
total_espaco_bytes = 0
usuarios = []

# Abrir o arquivo txt para leitura
arquivo = open('usuarios.txt', 'r')

#ler arquivo txt
for linha in arquivo:
    nome, espaco_bytes = linha.strip().split()
    espaco_bytes = int(espaco_bytes)
    total_espaco_bytes += espaco_bytes
    usuarios.append((nome, espaco_bytes))

#fechar o arquivo
arquivo.close()

#converte total para megabytes
total_espaco_mb = bytes_para_megabytes(total_espaco_bytes)

#ordena a lista de usuario, decrecente
usuarios.sort(key=lambda x: x[1], reverse=True)

#gerar o relatorio
print("ACME Inc.           Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------------------")
print("Nr.  Usuário         Espaço utilizado     % do uso")
for i, (nome, espaco_bytes) in enumerate(usuarios, start=1):
    espaco_mb = bytes_para_megabytes(espaco_bytes)
    percentual = calcular_percentual(espaco_bytes, total_espaco_bytes)
    print(f"{i:<4} {nome:<15} {espaco_mb:.2f} MB {'':>7} {percentual:.2f}%")

# Exibir o espaço total ocupado e médio ocupado
espaco_medio_mb = total_espaco_mb / len(usuarios)
print("\nEspaço total ocupado: {:.2f} MB".format(total_espaco_mb))
print("Espaço médio ocupado: {:.2f} MB".format(espaco_medio_mb))
