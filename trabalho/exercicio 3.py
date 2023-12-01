import os

caminho_desejado = r'C:\Users\fernando.silva8\Desktop\2023'

os.makedirs(os.path.join(caminho_desejado, 'Exercicio OS'))
os.makedirs(os.path.join(caminho_desejado, 'copia'))
os.makedirs(os.path.join(caminho_desejado, 'mover'))

for i in range(1, 4):
    nome_arquivo = f"exe0{i}.txt"
    caminho_arquivo = os.path.join(caminho_desejado, "Exercicio OS", nome_arquivo)

    with open(caminho_arquivo, 'w') as arquivo:
        pass
print('diretorios e arquivos criados com sucesso!')