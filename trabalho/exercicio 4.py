import os

caminho_desejado = r'C:\Users\fernando.silva8\Desktop\2023'

arquivos = os.listdir(caminho_desejado)

arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho_desejado, arquivo))]

print("Arquivos no diretório: ")
for arquivo in arquivos:
    print(arquivo)

