import os

caminho_desejado = "/caminho/para/seu/diretorio"  # Substitua pelo caminho correto

# Define o caminho completo para o arquivo a ser excluído
caminho_arquivo_a_excluir = os.path.join(caminho_desejado, "Exercicio OS", "exe03.txt")

# Verifique se o arquivo existe antes de tentar excluí-lo
if os.path.exists(caminho_arquivo_a_excluir):
    os.remove(caminho_arquivo_a_excluir)
    print("O arquivo 'exe03.txt' foi excluído com sucesso.")
else:
    print("O arquivo 'exe03.txt' não existe no diretório especificado.")