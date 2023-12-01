import os

caminho_desejado = r'C:\Users\fernando.silva8\Desktop\2023'

os.chdir(caminho_desejado)

novo_caminho = os.getcwd()
print('O diretorio atual agora é:', novo_caminho)